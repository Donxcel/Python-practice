from math import sqrt
import fractions
import os


def quadratic_1(a: int, b: int, c: int) -> object:
    test = (b ** 2 - (4 * a * c))
    quadratic_answer_1 = (-b + (sqrt(test))) / (2 * a)

    return quadratic_answer_1


def quadratic_2(a: int, b: int, c: int) -> object:
    test = (b ** 2 - (4 * a * c))
    quadratic_answer_2 = (-b - sqrt(test)) / (2 * a)
    return quadratic_answer_2


while True:
    print('this is the format\n ax^2+b^x+c')
    a = eval(input('enter the value of a'))
    b = eval(input('enter the value of b'))
    c = eval(input('enter the value of c'))
    total_1 = quadratic_1(a=a, b=b, c=c)
    total_2 = quadratic_2(a=a, b=b, c=c)
    print(f"the value of x1 is ={fractions.Fraction(total_1)}")
    print(f"the value of x2 is = {fractions.Fraction(total_2)}")
    condition = input('do you wan to clear the screen: "yes " or "no"')
    if condition == 'yes':
        os.system('cls')