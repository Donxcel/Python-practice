from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color('black')
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.speed("fastest")


    def moveUP(self):
        y = self.ycor()
        self.sety(y+10)

    def moveDown(self):
        y = self.ycor()
        self.sety(y - 10)
    def reset(self):
        self.penup()
        self.goto(0,-280)
#def creating the player