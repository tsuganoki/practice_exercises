"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
wrong_answer_list = [174, 175,200]

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

#jan 1 1901 is a Tuesday
months = [1,2,3,4,5,6,7,8,9,10,11,12]

def get_days(month,year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 9 or month ==  4 or month == 6 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def count_sundays():
    sundays = 0
    days_in_year = 1 # 1901 starts on a tuesday
    for year in range(1900,2001):
        for month in months:
            if days_in_year % 7 ==0:
                print("the first of",month,"in ",year,"was a sunday")
                sundays +=1
            days_in_year += get_days(month,year)
    return sundays

print(count_sundays())
