#!/user/bin/evn python3
# Copyright 2022 - edjata
# Working with Dates and Times
from datetime import datetime

day = datetime.today().day
month = datetime.today().month
year = datetime.today().year
day_of_month = day

today_date = datetime.today()
today_time = datetime.now()
time_now = datetime.now()

current_time = time_now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(str(day) + "/" + str(month) + "/" + str(year))
print(str(month) + "/" + str(day)  + "/" + str(year))
print(today_date)
print(today_time)
print(day_of_month)