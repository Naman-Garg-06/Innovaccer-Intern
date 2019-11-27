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
		entry = entry.split(' ')
		if entry[1] == guestEmail:
			CheckOutTime = strftime("%Y-%m-%d/%H:%M:%S", localtime())
			hostName = entry[4]
			message = "\nName: " + entry[0] + "\n" + "Phone: " + entry[2] + "\n" + "Check-in Time: " + entry[3] + "\n" + "Check-out Time: " + CheckOutTime + "\n"
			break
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
