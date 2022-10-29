from turtle import Turtle,Screen,color
import random
colors = ['DeepSkyBlue','wheat','SeaGreen','red','green','orange','blue','cyan','brown']
donal_turtle = Turtle()
donal_turtle.shape('classic')
play = [0,90,180,270]
donal_turtle.speed(5)
while True:
    donal_turtle.color(random.choice(colors))
    donal_turtle.width(5)
    donal_turtle.forward(40)
    donal_turtle.setheading(random.choice(play))


screen = Screen()
screen.exitonclick()

