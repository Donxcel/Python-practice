from turtle import Turtle
class Score(Turtle):
    def __init__(self,a,b):
        super(Score, self).__init__()
        self.score = 0
        self.player = 0
        self.color('white')
        self.penup()
        self.goto(a,b)
        self.hideturtle()

    def display(self,a,b):
         self.player = a
         self.score = b
         self.hideturtle()
         self.clear()
         self.write(f"player {self.player} \nscore: {self.score}",align="center",font=("Courier",30,"normal"))
    def winner(self,win):
        self.goto(0, 0)
        self.hideturtle()
        self.player = win

        self.write(f"player {self.player} scored a point",align="center",font = ("Courrier",30,"normal","bold"))
        self.clear()

