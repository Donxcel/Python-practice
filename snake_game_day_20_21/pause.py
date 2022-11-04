from turtle import Turtle
import time
PAUSING = False
class Pause(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed(0)
        self.hideturtle()

    def toggle_pause(self):

        return PAUSING
        self.write(f"GAME PAUSED ", align="center", font=("Courier", 41, "normal", "bold", "italic"))
        time.sleep(0.1)