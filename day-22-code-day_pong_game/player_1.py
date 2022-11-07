from turtle import Turtle
I = 280
class Player_1:
    def __init__(self):
        self.segments = []
    def add(self):
        for i in range(10):
            self.segments.append(self.create())

    def create(self):
        global I
        self.player = Turtle()
        self.player.color('white')
        self.player.shape('square')
        self.player.penup()
        self.player.speed('fastest')
        self.player.goto(-470,I)
        I+=10
    def moveUP(self):
        for test in self.segments:
            test.
