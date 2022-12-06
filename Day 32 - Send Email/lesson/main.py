### NOTE ###
"""
Using "smtplib" module to send email

1). Make sure you've got the correct smtp address for your email provider:
Gmail: smtp.gmail.com
Hotmail/Outlook: smtp.office365.com
Yahoo: smtp.mail.yahoo.com
if you use another email provider, just Google for your email provider e.g. "Gmail SMTP Address"

2). Make sure you've enabled less secure apps if you are sending from a Gmail account.
3). Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
4). Add a port number by changing your code to this:
smtplib.SMTP("smtp.gmail.com", port=587)

Simple Mail Transfer Protocol (SMTP)
Sender >> Gmail Mail Server >> Yahoo Mail Server >> recipient's computer

Email for Test: mailtesting9696@gmail.com and python100daytest@hotmail.com
Password: Qwerty!@#123
"""

# import smtplib

# my_email = "python100daytest@hotmail.com"
# password = "myymccmomgeapfmi" # App password

# with smtplib.SMTP("smtp.office365.com", port=587) as connection:
#     connection.starttls() # tls => transport layer security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="mailtesting9696@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt

now = dt.datetime.now() 
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week) # 0 = Sunday and so on

date_of_birth = dt.datetime(year=1997, month=3, day=15, hour=17, minute=17)
print(date_of_birth)