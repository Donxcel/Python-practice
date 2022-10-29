import random
import turtle
import time
import segment
# setting up the screen
delay = 0.1                         # estimated number of seconds
test  = ['up','down']
segments = []
test_random = random.choice(test)

def move():
    if snake.direction == "up":
        y = snake.ycor()            #y coordinates of the turtle
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()  # y coordinates of the turtle
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()            #x coordinates of the turtle
        snake.setx(x + 20)

    if snake.direction == "left":
        x = snake.xcor()            #y coordinates of the turtle
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
win.setup(width=800, height= 600)
win.tracer(0)                                  # creating the snake
snake= turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("green")
snake.penup()
snake.goto(0,100)
snake.direction = test_random
                                    #adding some food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.shapesize(0.5,0.5)
a= random.randint(-255,250)
b = random.randint(-255,250)
food.goto(a,b)
                            # adding new segment
                         # move the end segment in reverse order

win.listen()                # key bindings setting up the w,s,a,d keys
win.onkeypress(go_up,"w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

def new_segment():

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('square')
    new_segment.color('blue')
    new_segment.penup()
    segments.append(new_segment)
    if len(segments) == 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)
    else:
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

            print('true')
#main game loop

while True:
    win.update()
    move()
    time.sleep(delay)
    if snake.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment()

    print(len(segments))

