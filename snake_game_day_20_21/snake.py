from turtle import *
from random import *
import time
x = randint(-250,250)
y = randint(-250,250)

COORDINATES = ((0, 0), (-20, 0), (-40, 0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.direction = "Stop"
        self.create_snake()
    def create_snake(self):
        for i in COORDINATES:
            self.add_segment(i)

    def add_segment(self,POSITION):
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(POSITION)
        segment_1.speed(0)
        self.segments.append(segment_1)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def clearing(self):
        #print(len(self.segments))
        for i in range(0,(len(self.segments))):
            if i >2 :

                self.segments[i-1].hideturtle()
                self.segments[i-1].reset()

        del self.segments[2:-1]
        self.segments[0].goto(0,0)


    def move(self):

        print(len(self.segments))
        print(len(self.segments) - 1)
        for test in range(len(self.segments) - 1, 0, -1):
            x = self.segments[test - 1].xcor()
            y = self.segments[test - 1].ycor()
            self.segments[test].goto(x, y)
        self.segments[0].forward(20)
        # moving the snake using the arrow keys


    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)



    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)


    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)


    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)


    def collision(self):
        if self.segments[0].xcor() > 285 or self.segments[0].ycor() > 285 or self.segments[0].xcor() < -285 or self.segments[0].ycor() < -285 :
            self.segments[0].goto(0,0)
            new_pen = Turtle()
            new_pen.penup()
            new_pen.color("white")
            new_pen.speed(0)
            new_pen.hideturtle()
            new_pen.write(f"game over ", align="center",font=("Courier",41,"normal","bold","italic"))
            time.sleep(1)
            new_pen.clear()
            return True

