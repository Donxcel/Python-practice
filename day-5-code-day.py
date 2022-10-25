import random
from unittest import result
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','j','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['0','1','2','3','4','5','6','7','8','9']
letter =  eval(input("how many letters do you want for your password:  "))
symbol1 = eval(input("How many symbols would you like for your password:  "))
number =  eval(input("How many numbers do you want for your password: "))
random.shuffle(letters)
random.shuffle(symbols)
random.shuffle(numbers)
t =random.sample(letters,letter)
#print(''.join(t))
s =random.sample(numbers,number)
r =random.sample(symbols,symbol1)
result1 = []
result1 = t + s +r
random.shuffle(result1)
print(''.join(result1))
