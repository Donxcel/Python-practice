# building up a calculator
from msilib.schema import Condition


def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply

}
def calculator():
    num1 = eval(input("what's the first number:  "))
    for operation in operations:
        print(operation)
    test = input("what operation do you wanna perform:  ")

    num2 = eval(input("whats the second number: "))
    calculate = operations[test]
    answer = calculate(num1,num2)
    print(f" {num1} {test} {num2} = {answer}")
    Condition = 'y'
    while Condition:
        Condition = input(f' type "y"  to continue:  calculating with{answer} or "n" to exit or "start"')
        if Condition == 'y':
                get  = input('Input the operation:  ')
                num3 = eval(input("whats the  number: "))
                calculate1= operations[get]
                new_answer = calculate1(answer,num3)
                print(f" {answer} {get} {num3} = {new_answer}")
                answer = new_answer
        else:
            calculator()
calculator()
#recursion
