from turtle import *
FONT = ("Courier", 24, "normal", "bold")
ALIGN = 'center'
class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open('max_score.txt',mode='r') as text:
            self.high_score = int(text.read())
            print(self.high_score)
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(100,250)

        self.write(f"Score:0 High score:{self.high_score} ",align=ALIGN,font=FONT)
    def add_score(self,a,b):
        self.score = a
        b = self.high_score
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score} ", align=ALIGN, font=FONT)


