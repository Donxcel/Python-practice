from turtle import *
import pandas


def position(answer):
    t = Turtle()
    t.hideturtle()
    t.penup()
    new_answer = data[data.state == answer]
    t.goto(int(new_answer.x), int(new_answer.y))
    t.write(answer)


data = pandas.read_csv("./us-states-game-start/50_states.csv")
screen = Screen()
screen.title(f"states_in_the_US")
screen.setup(width=800, height=600)
screen.bgpic("./us-states-game-start/blank_states_img.gif")

i = 0
n = 0  # number of chances
new = [i for i in data.state]
while n <= 50:
    a = screen.textinput(title=f"{i}/50 us states", prompt="Enter one of the states")
    screen.update()
    str_a = a.title()
    if str_a == 'Exit':
        break
    for test in new:
        if str_a == test:
            store = new.index(str_a)
            position(str_a)
            new.pop(store)
            i += 1
    n += 1
print("These are the remaining cities you couldn't find")
print(new)
new_file = pandas.DataFrame(new)
new_file.to_csv("remaining_states.csv")
# checking to see the
