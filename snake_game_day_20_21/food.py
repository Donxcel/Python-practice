from turtle import Turtle
from random import randint

X = randint(-250, 250)
Y = randint(-250, 250)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('purple')
        self.speed("fastest")
        self.goto(X,Y)

    def new_position(self):
        x = randint(-250, 250)
        y = randint(-250, 250)
        self.goto(x,y)