# testing my skills
import programs
from turtle import *
from random import randint
is_race_start = False
import time
colors = ['red','orange','yellow','green','blue','purple']
screen = Screen()
collect_turtles = []
screen.title("donal")
screen.bgcolor("white")
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race")
y = 100

for i in  colors:
    player = Turtle(shape = "turtle")
    player.color(i)
    player.penup()
    player.goto(-290,y)
    collect_turtles.append(player)
    y-=50
if user_bet:
    is_race_start = True

while is_race_start:

    for test in collect_turtles:
        if test.xcor() > 290:
            wining = test.pencolor()
            if wining == user_bet:
                print("you won the bet ")
            else:
              print(f"wrong choice {wining} won the race")
            is_race_start = False
            programs.display(wining=wining)

        random_speed = randint(0,10)
        test.forward(random_speed)

while True:
    screen.update()