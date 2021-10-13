#Write a Python program that asks the user for their birth date and prints the user’s current age in years, months, and days.
#Sample output: You are 25 years, 4 months, and 22 days old

import datetime

print('Write your birthdate (mm/dd/yyyy):')

bdate = input('> ')

now_day = datetime.datetime.now().day
now_month = datetime.datetime.now().month
now_year = datetime.datetime.now().year

bdate_day = datetime.datetime.strptime(bdate, '%m/%d/%Y').day
bdate_month = datetime.datetime.strptime(bdate, '%m/%d/%Y').month
bdate_year = datetime.datetime.strptime(bdate, '%m/%d/%Y').year

if (now_month < bdate_month) or ((now_month == bdate_month) and (now_day < bdate_day)):
    years = now_year - bdate_year - 1
    months = 12 - (bdate_month - now_month)
else:
    years = now_year - bdate_year
    months = now_month - bdate_month


if bdate_day > now_day:
    if (now_month == 1) or (now_month == 3) or (now_month == 5) or (now_month == 7) or (now_month == 8) or (now_month == 10) or (now_month == 12):
        days = 31 - (bdate_day - now_day)
    elif (now_month == 2):
        if (now_year % 4 == 0):
                days = 29 - (bdate_day - now_day)
        else: 
            days = 28 - (bdate_day - now_day)
    else:
        days = 30 - (bdate_day - now_day)
else:
    days = now_day - bdate_day

print("You have ", years, "years, ", months,"months and ", days, "days")
