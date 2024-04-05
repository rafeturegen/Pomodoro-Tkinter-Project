from tkinter import *
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
timer_2 = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer_2)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer",fg=GREEN)
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps += 1
    if reps % 2 == 1:
        countdown(WORK_MIN*60)
        timer.config(text="Work",fg=GREEN)
    elif reps % 2 == 0 and not reps % 8 == 0:
        countdown(SHORT_BREAK_MIN*60)
        timer.config(text="Short Break",fg=PINK)
    else:
        countdown(LONG_BREAK_MIN*60)
        timer.config(text="Long Break",fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minute = int(count / 60)
    second = count % 60

    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")

    if count > 0:
        global timer_2
        timer_2 = window.after(1000, countdown, count - 1)
    elif count == 0:
        start_countdown()
        checkmark_label.config(text=int(reps / 2) * "✔", fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME, 35, "bold"),fill="white")
canvas.grid(row=1,column=1)


start_button = Button(text="Start",command=start_countdown)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",command=reset_time)
reset_button.grid(row=2,column=2)

timer = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME, 35, "bold"))
timer.grid(row=0,column=1)
checkmark_label = Label(bg=YELLOW)
checkmark_label.grid(row=3,column=1)
window.mainloop()