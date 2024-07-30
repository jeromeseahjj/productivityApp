# ---------------------------- IMPORTS---------------------------------- #
from tkinter import *
from tkinter import messagebox
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
reps = 0
timer = None
ongoing = False

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global ongoing
    # if ongoing:
    #     answer = messagebox.askyesno(title="Pomodoro", message="You have an ongoing pomodoro cycle, do you wish to reset?")
    #     if answer:
    #         reset_timer()
    # else:
    reps += 1
    ongoing = True
    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 6)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 6)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 6)

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_tick.config(text="")
    global reps
    global ongoing
    ongoing = False
    reps = 0
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    count_sec = f"0{count%60}" if count % 60 < 10 else count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        label_tick['text'] = "".join("✔" for i in range(reps))   
     


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)


# Canvas Widget allows you to layer things
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 122, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN)
label_timer.config(bg=YELLOW)
label_timer.grid(column=1, row=0)

label_tick = Label(text="", fg=GREEN, bg=YELLOW)
label_tick.grid(column=1, row=2)


start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
