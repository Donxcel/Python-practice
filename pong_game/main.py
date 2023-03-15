from turtle import *
from player_1 import Player
from time import sleep
from ball import Ball
from score import Score
from draw import Draw
import winsound



player1 = 1     # player one attributes
score1 = 0

player_2 = 2    # player two attributes
score2 = 0
sleeping = 0.05
screen  = Screen()
screen.title('PONG GAME')
screen.setup(width=1000,height=800)
screen.bgcolor('black')
screen.tracer(0)

# creation of player 1
p1 = Player(-450,0)
p2 = Player(450,0)
b1 = Ball()
score_1 = Score(-380,300)
score_2 = Score(380,300)
score_3 = Score(0,0)
drawing = Draw()
#input functions
screen.listen()
screen.onkeypress(fun=p1.moveUP,key='w')
screen.onkeypress(fun=p1.moveDOWN,key='s')

screen.onkeypress(fun=p2.moveUP,key='Up')
screen.onkeypress(fun=p2.moveDOWN,key='Down')


def initialise_position():
    p1.goto(-450, 0)  #
    p2.goto(450, 0)


def winning():
    global score1,sleeping
    score_3.winner(player1)
    sleep(2)
    score1 += 1
    b1.reset()
    sleeping = 0.05
    initialise_position()


def winning_2():
    global score2,sleeping
    score_3.winner(player_2)
    sleep(2)
    score2 += 1
    b1.reset()
    sleeping = 0.05

    initialise_position()
game_is_on = True
while game_is_on:

    sleep(sleeping)
    screen.update()
    score_1.display(player1,score1)
    score_2.display(player_2,score2)
    b1.move()
    if b1.ycor() > 380 or b1.ycor()< -380:
        winsound.PlaySound("sounds/beep-02.wav",winsound.SND_ASYNC)
        b1.bounce_y()

    # detect collision with right paddle
    if (b1.distance(p2) < 100 and b1.xcor() >420) or (b1.distance(p1) < 100 and b1.xcor() < -420):
        print("contact")
        winsound.PlaySound('sounds/boing.wav',winsound.SND_ASYNC)
        sleeping -= 0.001
        b1.bounce_x()


    if b1.xcor()> 500 :
        winsound.PlaySound("sounds/clap.wav",winsound.SND_ASYNC)
        winning()
    if b1.xcor() < -500:
        winsound.PlaySound("sounds/clap.wav", winsound.SND_ASYNC)
        winning_2()

    if score1 == 5:
        score_3.gameOver(player1,player_2)
        winsound.PlaySound("sounds/boo.wav", winsound.SND_ASYNC)
        screen.exitonclick()

    elif score2 == 5:
        score_3.gameOver(player_2,player1)
        winsound.PlaySound("sounds/boo.wav", winsound.SND_ASYNC)
        screen.exitonclick()


