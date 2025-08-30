import pandas
import datetime as dt
import smtplib
import random

#Variables
now = dt.datetime.now()
month = now.month
day = now.day
from_email = "marv4115@gmail.com"
to_email = ""
name = ""
password = "kwmo aoni yodd naok"

#Functions
def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print(from_email, )
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=f"Subject: Happy Bday\n\n"
                                f"{message}")
        
def generate_email():
    num = random.randint(1,3)
    with open(f"letter_templates/letter_{num}.txt", "r") as email_temp:
        contents = email_temp.read()
        new_contents = contents.replace("[NAME]", name)
    return new_contents
 
#Import CVS using pandas
df = pandas.read_csv("birthdays.csv")

#Iterate over data frame to see if a birthday matches today
for (index,row) in df.iterrows():
    if row.month == month and row.day == day:
        to_email = row["email"]
        name = row["name"]
        send_email(generate_email())
       




