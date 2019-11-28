# guest while checking out, enters his email id as it will
# be unique among all guests. At the end of the code, guest
# will get a mail regarding his stay.

from time import localtime, strftime
import smtplib
from checkin import siteManager

def guestDetail():
    print("Guest Email_Id: ",end="")
    guestEmail = input()
    CheckOutTime = ""
    message = ""
    hostName = ""
    file = open(r"Guest_Info", "r")
    for entry in file.readlines():

        temp_entry = entry.split('@')
        left_entry = temp_entry[0].split()
        right_entry = temp_entry[1].split()
        left_len = len(left_entry)
        right_len = len(right_entry)

        if left_entry[-1] + '@' + right_entry[0] == guestEmail:
            CheckOutTime = strftime("%H:%M:%S", localtime())
            guestName = ''
            for i in range(left_len-1):
                guestName = guestName + left_entry[i] + " "
            hostName = ''
            for i in range(3,right_len):
                hostName = hostName + right_entry[i] + ' '
            message = "\nName: " + guestName + "\n" + "Phone: " + right_entry[1] + "\n" + "Check-in Time: " + right_entry[2] + "\n" + "Check-out Time: " + CheckOutTime + "\n"
    emailToGuest(message, guestEmail, hostName)

def emailToGuest(bodytext, guestEmail, hostName):

    objSiteManager = siteManager()
    address,account_sid,auth_token,twiliocontact,emailLoginId,emailLoginPassword = objSiteManager.siteManagerInfo()
    
    bodytext += "Host Name: " + hostName + "\n" + "Address Visited: " + address
    
    subject = "Your meet at " + address + "."
    message = 'Subject: {}\n\n{}'.format(subject, bodytext)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(emailLoginId, emailLoginPassword)
    try:
        s.sendmail(emailLoginId, guestEmail, message)
        print("Guest Check-out Successful")
    except:
        print("Unable to Check-out.")
    s.quit()

if __name__ == "__main__":
    guestDetail()