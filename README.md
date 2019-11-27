# Innovaccer-Intern
Summer Internship Challenge Hiring - **Innovaccer**

### Prerequisites
All the Scripts that I have created have been tested on Ubuntu-18.04 with python version 3.6.  
The Mail sent to Guest and Host is done via **smtp** library.  
The SMS sent to Host is done via **twilio** library.  
**time** library is imported to store the entry with the timestamp of entry.

### How it Works?
There are two scripts: checkin.py and checkout.py  
Also there are **three** parties involved. One is the *Guest*, second is the *Host* with whom guest is meeting and third will be the *site manager* or the middle person.      
The site manager has to set up a **twilio** account, details of how to do it is given in the *setup.txt* file. The manager also sets up a gmail account to send emails to the Host at check-in and to the Guest at check-out.  
Once the manager runs the *checkin.py* script, it prompts the guest to enter his name, contact and email; the script also prompts to enter the Host info.  
After the check-in, the host recieves a mail through **smtp** regarding the guest details and the check-in-time.  
![](https://github.com/Naman-Garg-06/Innovaccer-Intern/blob/master/Mail_to_Host.png)  

Also an sms is sent through **twilio** with the same details.  

At check-out, Guest enters his e-mail id which extracts his info from the **Guest_Info** database. Again using the **time** library the check-out time is taken and the Guest recieves a mail from the manager regarding his meeting with the Host.    
After Check-in, Host will recieve the mail in the following format.  
![](https://github.com/Naman-Garg-06/Innovaccer-Intern/blob/master/HostMail.png)  

After Check-out, Guest will recieve the mail in the following format.  
![](https://github.com/Naman-Garg-06/Innovaccer-Intern/blob/master/GuestMail.jpeg)   

**NOTE: While entering the phone number, make sure you start with +91 and then the number**
