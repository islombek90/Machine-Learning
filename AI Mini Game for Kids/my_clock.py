import time
from tkinter import *
import math

import ui_setup

start_time = time.monotonic()

def get_counter():
    current_time = time.monotonic()

    return int(current_time - start_time)



# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

timer_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = timer_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_canvas.grid(column=1, row=1)



# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    ui_setup.windows.after_cancel(timer)
    timer_canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = WORK_MIN * 60
    count_down(work_sec)
    title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(counter):

    count_min = math.floor(counter / 60)
    count_sec = counter % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if counter > 0:
        global timer
        timer = ui_setup.windows.after(1000, count_down, counter - 1)
    else:
        start_timer()











