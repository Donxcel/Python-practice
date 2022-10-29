from turtle import *
donal_turtle = Turtle()
donal_turtle.width(3)
for i in range(6):
    for color in ('red', 'magenta', 'blue',
                      'cyan', 'green', 'brown',
                      'yellow'):
            donal_turtle.color(color)
            donal_turtle.circle(100)
            donal_turtle.left(10)

screen = Screen()
screen.exitonclick()