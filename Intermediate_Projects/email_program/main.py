# import smtplib
#
# email = "marv4115@gmail.com"
# password = "kwmo aoni yodd naok"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email,
#                         to_addrs="logic4115@hotmail.com",
#                         msg="Subject: Hello\n\nThis is the body of the email")
#


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

birthday = dt.datetime(year=1988, month=3, day=4)
print(birthday)