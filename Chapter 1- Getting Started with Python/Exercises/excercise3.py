# Write a Python program to display the current date and time in simple codes.

import datetime
now = datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%Y-%M-%D %H:%M:%S"))