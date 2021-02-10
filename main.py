import pandas
import datetime as dt
import random
import smtplib
now = dt.datetime.now()

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = ""
my_password = ""

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

for person in data_dict:
    if person["month"] == now.month and person["day"] == now.day:
        name = person["name"]
        email = person["email"]

        with open(f"./letter_templates/{random.choice(letters)}") as file_letters:
            letter_lines = file_letters.readlines()
            letter_string = ""
            for line in letter_lines:
                letter_string += line

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject: Happy Birthday \n\n {letter_string.replace('[NAME]', name)}")








