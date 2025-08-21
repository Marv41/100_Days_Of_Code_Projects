from tkinter import *
from tkinter import Label


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
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    fsec = count % 60
    fmin = count // 60
    canvas.itemconfig(timer_text, text=f"{fmin}:{fsec:02d}")
    # canvas.itemconfig(timer_text, text=f"{count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        num_of_checkmarks = reps // 2
        marks = ""
        for _ in range(num_of_checkmarks):
            marks += "✔"
            check_mark.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=GREEN, fg="white", font=(FONT_NAME, 16, "bold"), highlightthickness=0, bd=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", bg=GREEN, fg="white", font=(FONT_NAME, 16, "bold"), highlightthickness=0, bd=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)


window.mainloop()