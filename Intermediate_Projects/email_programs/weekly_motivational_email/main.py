import smtplib
import datetime as dt
import random

email = "marv4115@gmail.com"
password = "kwmo aoni yodd naok"
now = dt.datetime.now()
day = now.weekday()

def send_email(message):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="marv4115@gmail.com",
                            msg=f"Subject: Weekly Motivational Quote\n\n{message}")

if day == 4:
    with open("quotes.txt", "r") as file:
        print("sending email")
        quotes = file.readlines()
        send_email(random.choice(quotes))

