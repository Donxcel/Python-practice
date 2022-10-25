from calendar import month
from re import L


def leap_year(year):
    if year%4 == 0:
        if year%100  == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def days_in_month(month,year):
    test = leap_year(year)
    if test == False:
        month_days = [31,28,30,31,30,31,31,31,30,31,30,31]
    else:
        month_days =[31,29,30,31,30,31,31,31,30,31,30,31]
    return month_days[month-1]
years = eval(input("Input the year"))
months= eval(input("input the month:"))
days  = days_in_month(month = months,year = years)
print(days)
'''
this is a comment

'''