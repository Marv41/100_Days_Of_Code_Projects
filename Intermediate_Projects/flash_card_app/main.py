from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
count_down_time = 3
timer = None

#Change card image and update text after 3 seconds

def count_down(count):
    global timer

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        canvas.itemconfig(card, image=card_front)
        canvas.itemconfig(card_text, text="English Translation")

def right_answer():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_text, text="next spanish word")
    count_down(count_down_time)

def wrong_answer():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_text, text="next spanish word")
    count_down(count_down_time)



window = Tk()
window.title("Flashy")


canvas = Canvas(width=900, height=726, bg=BACKGROUND_COLOR)
canvas.pack()

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

card = canvas.create_image(450, 313, image=card_back)

wrong_button = Button(image=wrong, command=wrong_answer)
canvas.create_window(200, 651, window=wrong_button)

right_button = Button(image=right, command=right_answer)
canvas.create_window(700, 651, window=right_button)

card_text = canvas.create_text(450, 313, text="Spanish Word")



count_down(count_down_time)

window.mainloop()