# simple entry management software
# user enters the details as prompted in the terminal
# code runs and sends the information to the host.
# also another file runs and it is for checkout.
# guest enters his name and checkout time and recieves
# info regarding his stay.

import smtplib
from twilio.rest import Client
from time import localtime, strftime

class siteManager:
    def siteManagerInfo(self):
        address = "LNMIIT"
        account_sid = 'AC17191c56db80ec90f48a614acbe6ee19'
        auth_token = 'fcb3dda668dbf2e93e702a07775d816a'
        twilioContact = '+14842026039'
        emailLoginId = "namannitish98@gmail.com"
        emailLoginPassword = "Naman8009688668"
        return address,account_sid,auth_token,twilioContact,emailLoginId,emailLoginPassword

def hostDetails():
    print("Host Name:" ,end=" ")
    hostName = input()
    print("Host Phone:" ,end=" ")
    hostPhone = input()
    print("Host Email:" ,end=" ")
    hostEmail = input()
    storeHostInfo(hostName,hostPhone,hostEmail)

def storeHostInfo(hostName, hostPhone, hostEmail):
    file = open(r"Host_Info","a")
    for L in [hostName, " ", hostEmail, " ", hostPhone]:
        file.writelines(L)
    file.writelines("\n")
    file.close()
    guestDetails(hostName)

def guestDetails(hostName):
    print("Guest Name:",end=" ")
    guestName = input()
    print("Guest Phone:",end=" ")
    guestPhone = input()
    print("Guest Email:" ,end=" ")
    guestEmail = input()
    
    CheckinTime = strftime("%Y-%m-%d/%H:%M:%S", localtime())
    
    storeGuestInfo(guestName, guestEmail, guestPhone, CheckinTime, hostName)

def storeGuestInfo(guestName, guestEmail, guestPhone, CheckinTime, hostName):
    file = open(r"Guest_Info","a")
    for L in [guestName, " ", guestEmail, " ", guestPhone, " ", CheckinTime, " ", hostName]:
        file.writelines(L)
    file.writelines("\n")
    file.close()

    message = "\nName: " + guestName + "\n" "Email: " + guestEmail + "\n" + "Phone: " + guestPhone + "\n" + "Check-in Time: " + CheckinTime
    
    emailToHost(message,hostName)

def emailToHost(bodytext, hostName):

    objSiteManager = siteManager()
    address,account_sid,auth_token,twilioContact,emailLoginId,emailLoginPassword = objSiteManager.siteManagerInfo()

    hostPhone = ""
    hostEmail = ""
    file = open(r"Host_Info", "r")
    for entry in file.readlines():
        entry = entry.split()
        if entry[0] == hostName:
            hostPhone = entry[2]
            hostEmail = entry[1]

    subject = "Guest meet at " + address + "."
    message = 'Subject: {}\n\n{}'.format(subject, bodytext)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(emailLoginId, emailLoginPassword)
    
    try:
        s.sendmail(emailLoginId, hostEmail, message)
        print("Guest Check-in Successful")
    except:
        print("Failed")
    s.quit()
    
    smsToHost(message,account_sid,auth_token,twilioContact,hostPhone)

# sending message to host
def smsToHost(message,account_sid,auth_token,twilioContact,hostPhone):

    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                              from_= twilioContact, 
                              body = message, 
                              to = hostPhone
                          )

if __name__ == "__main__":
    hostDetails()