# testing my skills
from turtle import *
import time
screen = Screen()
player = Turtle()
screen.title("donal")
screen.bgcolor("green")
screen.setup(width=600,height=400)
# player properties
player.penup()
player.speed(2)

def move():
     player.forward(1000)
screen.listen()
screen.onkey(key="space",fun=move)
while True:
    screen.update()
    time.sleep(0)