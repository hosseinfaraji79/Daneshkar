
import datetime
import jdatetime
"""
Reading the date of birth
"""

birthday_str = input('Please enter your birthday (yyyy-mm-dd):')
birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d')

"""
Calculation of total seconds of life
"""

difference = datetime.datetime.now()
total_seconds = difference.total_seconds()
print((f'Total seconds of your age: ', {total_seconds}))

"""
Convert date of birth to Jalali calendar
"""

j_date = jdatetime.date.fromgregorian(date=birthday)
print(f'Your birthday in Jalali calender: , {j_date.strftime("%A,%d,%B,%y")}')