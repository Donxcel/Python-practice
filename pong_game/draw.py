from turtle import Turtle
class Draw(Turtle):
    def __init__(self):
        super(Draw, self).__init__()
        self.color('white')
        self.penup()
        self.goto(0,390)
        self.setheading(270)
        self.pendown()
        self.hideturtle()
        self.goto(0,-400)