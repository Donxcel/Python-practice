from turtle import *
def display(wining):
    pen = Turtle()
    pen.penup()
    pen.speed(0)
    pen.hideturtle()
    pen.color('black')
    pen.goto(0, 150)
    pen.write("{} turtle won the race".format(wining), align='center', font=('Courier', 24, 'normal'))

