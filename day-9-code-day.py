from msilib.schema import Condition
import os

biders = {}
print("welcome to the secret auction Program")
def add_biders(name,price):
   biders[name] = price 
condition = True
while Condition:
    get_name = input("what is your name:  ")
    get_bid = eval(input('Enter your bid: $'))
    add_biders(get_name,get_bid)
    test = input("is there another bidder 'yes' or 'no'")
    if test == 'no':
        condition = False
        break
    elif test == 'yes':
        os.system('cls') 

#print(biders)
max=0
for bigger in biders:
    if max > biders[bigger]:
        max = max
    else:
        max = biders[bigger]
    #print(type(biders[bigger]))
#print(max)
    for bigger in biders:
        if biders[bigger] == max:
            print(f"the winner is {bigger} with a price of ${biders[bigger]}")