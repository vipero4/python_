# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

now = datetime.datetime.now()
user_name = input("Whats your name? ")
user_age = int(input("Whats your age? "))
age_100 = (100 - user_age) + now.year

print("Hello {}, you will turn 100 years old in {}.".format(user_name, age_100))
