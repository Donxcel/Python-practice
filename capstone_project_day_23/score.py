from turtle import Turtle
class Score(Turtle):
    def __init__(self,a):
        self.level = a
        super(Score, self).__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-290,250)
        self.write(f"level : {self.level}",align="center",font=("Courier",30,"normal"))
        #self.clear()

    def update(self,a):
        self.clear()
        self.level = a
        self.penup()
        self.goto(-290, 250)
        self.write(f"level : {self.level}", align="center", font=("Courier", 30, "normal"))
    def gameOver(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"game over", align="center", font=("Courier", 30, "normal"))