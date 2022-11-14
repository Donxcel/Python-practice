from turtle import Turtle
from random import randint,choice
import time
COLORS= ['red','green','brown','blue','cyan','magenta',]

class Cars:
    def __init__(self):
        self.listing = []
        self.increment = 10
    def create(self):
        ran = randint(1,5)
        if ran == 1:
            a = Turtle()
            a.color(choice(COLORS))
            a.shape("square")
            a.shapesize(1,2)
            x = randint(-230,230)
            a.penup()
            a.speed(0)
            a.goto(300,x)
            self.listing.append(a)
        self.move()
    def move(self):
        for test in self.listing:
            test.backward(self.increment)