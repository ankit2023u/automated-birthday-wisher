##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
##################### Hard Starting Project ######################

import pandas as p
import datetime as dt
from random import randint
import smtplib

# Part 1 - Importing the data
raw_data = p.read_csv('birthdays.csv')
birthday_list = raw_data.to_dict(orient='records')
my_email = "rwoodland32145@gmail.com"
my_pass = "12#45^78A"

# Part 2 - Matching a birthday
today = dt.datetime.now()
for birthday in birthday_list:
    if birthday['month'] == today.month and birthday['day'] == today.day:

        # Part 3 - Creating a letter
        with open(f'letter_templates/letter_{randint(1,3)}.txt') as letter:
            raw_message = letter.read()
            corrected_message = raw_message.replace('[NAME]', birthday['name'])

        # Part 4 - Sending the mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Make connection secure
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday['email'],
                                msg=f"Subject:Happy Birthday\n\n{corrected_message}"
                                )
