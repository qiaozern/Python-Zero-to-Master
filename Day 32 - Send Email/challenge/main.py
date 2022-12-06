### Monday Quote ###
import datetime as dt
import smtplib
import random

MY_EMAIL = "python100daytest@hotmail.com"
PASSWORD = "myymccmomgeapfmi" # App password

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        random_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="zernnnnn_@hotmail.com",
            msg=f"Subject:Quote of the day\n\n{random_quote}"
        )