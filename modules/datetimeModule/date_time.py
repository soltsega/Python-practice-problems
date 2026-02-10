# datetime module in python
# datetime is a module in python that provides a way to work with date and time
# datetime is imported from the datetime module
import datetime

# practical use cases
# 1. to get the current date and time
today = datetime.datetime.now()
print(today)  # 2023-09-04 11:30:00  with a format of year-month-day hour:minute:second

# strftime() method is used to format the data and time in a specified way
print(today.strftime("%Y-%m-%d %H:%M:%S"))


# 2. to create a date object
date = datetime.date(2023, 9, 4)
print(date)