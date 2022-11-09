from turtle import Turtle


class Player(Turtle):
    def __init__(self, a, b):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.shapesize(5, 0.5)
        self.goto(a, b)

    def moveUP(self):
        new = self.ycor() + 15
        self.goto(self.xcor(), new)

    def moveDOWN(self):
        new = self.ycor() - 15
        self.goto(self.xcor(), new)
    def initialise(self):
        pass