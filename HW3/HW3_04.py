from datetime import datetime
import jdatetime


# Taking Inputs from User
year, month, day = input("Please Enter your Birth date\
in format yyyy/mm/dd: ").split("/")
year, month, day = int(year), int(month), int(day)
print("\n************************************************\n")


# Age in Seconds
org = datetime(year, month, day)
now = datetime.now()
delta1 = (now - org).total_seconds()
print(f"You are {delta1} seconds old")
print("\n************************************************\n")


# Minutes and days remaining to next birthday
if (month <= now.month) and (day > now.day):
    delta = datetime(now.year, org.month, org.day) - now
    d_days, d_mins = delta.days + 1, delta.total_seconds() / 60
else:
    delta = datetime(now.year + 1, org.month, org.day) - now
    d_days, d_mins = delta.days + 1, delta.total_seconds() / 60
print(f"{d_days} days and {d_mins} minutes remaining to your next birthday.")
print("\n************************************************\n")


# Converting birth date to Jalali format
jalali = jdatetime.date.fromgregorian(day=day, month=month, year=year)
print(f"Your Birthdate in Jalali format is {str(jalali)}")