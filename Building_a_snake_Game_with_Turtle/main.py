import random
import turtle
import time
import segment

# setting up the screen
delay = 0.04  # estimated number of seconds
test = ['up', 'down']
segments = []
test_random = random.choice(test)
score = 0                               # initialising the scores
high_score = 0

def move():
    if snake.direction == "up":
        y = snake.ycor()  # y coordinates of the turtle
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()  # y coordinates of the turtle
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()  # x coordinates of the turtle
        snake.setx(x + 20)

    if snake.direction == "left":
        x = snake.xcor()  # y coordinates of the turtle
        snake.setx(x - 20)


def go_up():
    if snake.direction != "down":
        snake.direction = 'up'


def go_down():
    if snake.direction != "up":
        snake.direction = 'down'


def go_left():
    if snake.direction != "right":
        snake.direction = 'left'


def go_right():
    if snake.direction != "left":
        snake.direction = 'right'

        # main code


win = turtle.Screen()
win.title("DONXCEL_SNAKE GAME")
win.bgcolor("black")
win.setup(width=700, height=600)
win.tracer(0)  # creating the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("green")
snake.penup()
snake.goto(0, 100)
snake.direction = test_random
# adding some food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.shapesize(0.5, 0.5)
a = random.randint(-250, 250)
b = random.randint(-250, 250)
food.goto(a, b)
# adding new segment
# move the end segment in reverse order

win.listen()  # key bindings setting up the w,s,a,d keys
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")
                        #adding the scores in the game
pen = turtle.Turtle()
pen.speed(0)
#pen.shape("square")
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

new_segment = turtle.Turtle()
def new_segments():

    new_segment.speed(0)
    new_segment.shape('square')
    new_segment.color('blue')
    new_segment.penup()
    segments.append(new_segment)
    if len(segments) == 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
        print(x,y)

    for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)


def collision():
    if snake.xcor() > 350 or snake.xcor() < -350 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(0.85)
        snake.goto(0,0)
        snake.direction = "down"
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        print(x,y)
        global score
        global high_score
        if score > high_score:
            high_score = score
        score = 0
        pen.clear()
        pen.write("score:0 High Score:{}".format(high_score), align="center", font=("Courier", 24, "normal"))


# main game loop

while True:
    win.update()
    move()
    time.sleep(delay)
    if snake.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segments()
        score += 1
        pen.clear()
        pen.write("score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))



    collision()
