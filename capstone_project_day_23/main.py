from turtle import Screen
from player import Player
from cars import Cars
from score import Score
from time import sleep
#  position of the cars on the screen

## current level
level = 0
tester = 0.3

#screen parameters
screen = Screen()
screen.setup(width=800,height=600)
screen.title("cross the road")
screen.bgcolor("white")
screen.tracer(0)

#  player parameters

player_1 = Player()
moto = Cars()
scoring  = Score(level)
#  listening to the screen
screen.listen()
screen.onkey(key="Up",fun=player_1.moveUP)
screen.onkey(key="Down",fun=player_1.moveDown)

game_is_on = True
while game_is_on:

    screen.update()
    sleep(0.09)
    moto.create()
    print(moto.increment)
    for i in moto.listing:
        if player_1.distance(i) < 20:
            print('passed')
            scoring.gameOver()
            screen.exitonclick()
        if player_1.ycor() > 290:
            level += 1
            player_1.reset()
            sleep(1)
            scoring.update(level)
            moto.increment += 10
