from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.speed(0)
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
            y = self.ycor() + self.y_move
            x = self.xcor() + self.x_move
            self.goto(x,y)
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_p(self):
        self.x_move *= 1

    def reset(self):
        self.penup()
        self.goto(0,0)






