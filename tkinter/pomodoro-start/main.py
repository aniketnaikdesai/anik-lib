from cProfile import label
from cgitb import text
from curses import window
from glob import glob
from itertools import count
import math
from tkinter import *
from tkinter import font
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_id = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_id, reps
    reps = 0
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text,text='00:00')
    check_marks.config(text='')
    title_lable.config(text='Timer',fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text='Long Break',fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lable.config(text='Short Break',fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text='Work',fg=GREEN)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    global timer_id
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count>0:
        timer_id = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks =''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +='✔'
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)

title_lable = Label(text='Timer', fg=GREEN, bg=YELLOW,font=(FONT_NAME,50))
title_lable.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='Tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text='00:00', fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

start_button = Button(text='Start',highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
check_marks.grid(column=1,row=2)



window.mainloop()