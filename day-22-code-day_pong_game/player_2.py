from player_1 import Player_1
from turtle import Turtle
I = 280
class Player_2(Player_1):
    def __init__(self):
        super(Player_2, self).__init__()
        self.add()
    def create(self):
        global I
        self.player = Turtle()
        self.player.color('white')
        self.player.shape('square')
        self.player.penup()
        self.player.speed('fastest')
        self.player.goto(470, I)
        I += 10