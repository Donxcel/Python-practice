from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_SYMBOL = "✓"
reps = 1
i = 1  # checking for a round

main_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(main_timer)
    tick.config(text="")
    label_1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        label_1.config(text="Get to work ", fg=RED)
    elif reps == 8:
        count_down(long_break)
    elif reps % 2 == 0:
        count_down(short_break)
        label_1.config(text="Take a rest ", fg=GREEN)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_min)) == 1:
        count_min = f'0{count_min}'
    if len(str(count_sec)) == 1:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count != 0:
        global main_timer
        main_timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        global i
        if reps % 2 == 0:
            tick.config(text=TICK_SYMBOL * i)
            i += 1
        if i == 4:
            tick.config(text="done for today, go get a rest")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomadoro")
window.size()
window.config(pady=100, padx=80, bg=PINK)

# creating the label "timer"
label_1 = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=PINK)
label_1.grid(column=2, row=1)

# creating the start button
start_button = Button(text="start", width=6, command=start_timer)
start_button.config(bg=GREEN)
start_button.grid(column=1, row=10)

# creating the stop button
stop_button = Button(text='stop', width=6, highlightthickness=0, command=reset)
stop_button.config(bg=GREEN)
stop_button.grid(column=4, row=10)

# CREATING THE TICK LABEL
tick = Label(text="", fg=GREEN, font=(FONT_NAME, 20, 'bold'), bg=PINK, highlightthickness=0)
tick.grid(column=2, row=10)

# creating a canvas
canvas = Canvas(width=220, height=220, bg=PINK, highlightthickness=0)
get_image = PhotoImage(file="tomato.png")  # getting the image

canvas.create_image(100, 100, image=get_image)
timer_text = canvas.create_text(100, 120, text="00:00", font=(FONT_NAME, 30, 'bold'), fill="white")
canvas.grid(column=2, row=7)

window.mainloop()
