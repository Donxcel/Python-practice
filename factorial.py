# creating a function
from random import *

getting_list = []
print("enter your name")
string_name = input("")
getting_list = list(string_name)
shuffle(getting_list)
yo = sample(getting_list, 2)
print(getting_list)
print(yo)


def factorial(number):
    total = 1
    if number == 1 or number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            total = total * i
        return total


get_num = eval(input("enter a number to get the factorial: "))
print(f"{get_num}! is :{factorial(number=get_num)}")
