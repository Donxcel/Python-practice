from random import *
random_number = randint(1,100) # generating the random number
#GUESSING A NUMBER
chances  = 0
loop_1 = True
print("welcome to the number guessing game: ")
print("i am thinking of a number between 1 to 100")
level = input("do you want the 'easy' or 'hard' level:  ").lower()

print(random_number)
if level == 'easy':
    chances = 10
else:
    chances = 5
while loop_1:
    print(f'you have {chances} attempt to go:  ')
    get =eval(input("guess the number:  "))
    if get == random_number:
        print(f'Excellent guess you won the game \nthe number was  {random_number}')
        loop_1 = False
    else:
        if get > random_number:
            print("the number is smaller")
        else:
           
                print('the number is bigger')
        chances-=1
    if chances == 0:
        print(" you ran out of life better luck next time!!!")
        loop_1 = False