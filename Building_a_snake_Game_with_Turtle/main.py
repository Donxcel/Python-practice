import turtle
import time
# setting up the screen
delay = 0.1                         # estimated number of seconds


def move():
    if snake.direction == "up":
        y = snake.ycor()            #y coordinates of the turtle
        snake.sety(y + 20)


    if snake.direction == "down":
        y = snake.ycor()  # y coordinates of the turtle
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()            #x coordinates of the turtle
        snake.sety(x + 20)

    if snake.direction == "left":
        x = snake.xcor()            #y coordinates of the turtle
        snake.sety(x + 20)
win = turtle.Screen()
win.title("DONXCEL_SNAKE GAME")
win.bgcolor("black")
win.setup(width=800, height= 600)
win.tracer(0)
# creating the snake
snake= turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,50)
snake.direction = "stop"

#main game loop
while True:
    win.update()
    move()
    time.sleep(delay)