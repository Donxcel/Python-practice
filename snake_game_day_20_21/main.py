from turtle import *
from snake import Snake
from food import Food
from score import Score
from pause import Pause
import time
delay =0.08
screen  = Screen()
score = 0
h_score = 0
final = 0
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

new_Snake = Snake()
new_food = Food()
new_score = Score()
pause_game = Pause()
# checking input from the keyboard

screen.listen()
screen.onkey(key="Up",fun=new_Snake.up)
screen.onkey(key="Down",fun=new_Snake.down)
screen.onkey(key="Left",fun=new_Snake.left)
screen.onkey(key="Right",fun=new_Snake.right)
#screen.onkey(key="p", fun=new_Snake.pause)

is_game_true = True
def toggle():
    pausing = Pause()
    pausing.toggle_pause()
    time.sleep(5)
def game_failed():
    new_food.new_position()
    new_pen = Turtle()
    new_pen.penup()
    new_pen.color("white")
    new_pen.speed(0)
    new_pen.hideturtle()
    new_pen.write(f"game over ", align="center", font=("Courier", 41, "normal", "bold", "italic"))
    time.sleep(1)
    new_pen.clear()
screen.onkey(key='p',fun=toggle)
while is_game_true:

    if score > h_score:
        h_score = score
    screen.update()
    new_Snake.move()
    time.sleep(delay)


    # detect collision with tale
    for snake in new_Snake.segments:
        if snake == new_Snake.segments[0]:
            pass
        elif new_Snake.segments[0].distance(snake)<10:
            final = h_score
            score = 0
            game_failed()
            get = screen.textinput(title='GAME OVER', prompt="Do you want to PLay again").lower()
            screen.listen()
            new_Snake.clearing()

    #detect collision  with food
    if new_Snake.segments[0].distance(new_food) < 15:
        new_food.new_position()
        new_Snake.extend()
        score += 1



    if new_Snake.collision() == True:
        final = h_score
        score = 0
        new_food.new_position()

        get = screen.textinput(title='GAME OVER',prompt="Do you want to PLay again").lower()
        screen.listen()
        new_Snake.clearing()

        # condition to continue or not
        if get == 'no' or get == 'n':
            is_game_true = False

    new_score.add_score(score, final)
with open('max_score.txt', mode='w') as store:
    store.write(str(final))