# creating a simple black jack game
# and the game is well completed
from msilib.schema import Condition
from secrets import choice
from webbrowser import get
import os

list_user = []
list_computer = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def sum_cards(list_user):
    return sum(list_user)
    # main function


def user_card(list_user):
    user_card = choice(cards)
    return list_user.append(user_card)


def computer_card(list_computer):
    computer_card = choice(cards)
    list_computer.append(computer_card)


def start():
    os.system('cls')
    get = input('do you want to play a game of black jack:  "y" or "n"')
    if get == 'y':

        print("let's start a new round")
    else:
        print("Exiting the game")
        exit()


def start_over():
    if input('do you want to start over "y"') == 'y':
        list_user.clear()
        list_computer.clear()
        start()
    else:
        print("thankyou for playing our game")
        exit()


damn = True
start()
# test condition


output_3 = 0  # to get the sum of [0] and [1] for computer

text = 0  # condition to test if the first and second number are less than 17
while True:
    getting = input("input 'hit' to get your card:   ").lower()
    if getting == 'hit':
        computer_card(list_computer=list_computer)
        user_card(list_user=list_user)
        output_1 = sum_cards(list_user)
        output_2 = sum_cards(list_computer)

        print(f'u have the number {list_user} and the sum is {output_1}')
        print(f'the computer have the number {list_computer[0]} ')
        if len(list_computer) == 2:
            for inside in range(2):
                output_3 = sum(list_computer)
        # print(output_3)
        if len(list_computer) > 2 and output_3 < 17:  ########test condition to see if first and scond card are less than 17
            text = choice(cards)
            # print(type(text))
            output_3 = output_3 + text
        if output_1 > 21:
            print(f"the computer won with {output_3} you lose :  ")
            print(f"you scored {output_1}")
            start_over()

        elif output_3 > 21:
            print(f"you won the game with {output_1} \n wwll done!!!!")
            print(f"the computer scored {output_3}")
            start_over()

        decision = input("do you want to hit once more or stop:   'y' or 'n'")

        if decision == 'y':
            damn = True

        else:
            if output_1 == 21 and output_3 != 21:
                print('you win')
                print(f"you scored {output_1} meanwhile the computer scored {output_3}")
                start_over()
            elif output_1 != 21 and output_3 == 21:
                print('the computer won')
                print(f"you scored {output_1} meanwhile the computer scored {output_3}")
                start_over()
            elif output_1 == 21 and output_3 == 21:
                print("it's a draw")
                print(f"you scored {output_1} meanwhile the computer scored {output_3}")
                start_over()
            elif output_1 < 21 and output_3 < 21 and output_1 > output_3:
                print('you win')
                print(f"you scored {output_1} meanwhile the computer scored {output_3}")
                start_over()
            elif output_1 < 21 and output_3 < 21 and output_1 < output_3:
                print('the computer won')
                print(f"you scored {output_1} meanwhile the computer scored {output_3}")
                start_over()
            elif output_1 < 21 and output_3 < 21 and output_1 == output_3:
                print("it's a draw")
                print(f"you scored {output_1} meanwhile the computer scored {output_3}")
                start_over()
    else:
        Condition = False
