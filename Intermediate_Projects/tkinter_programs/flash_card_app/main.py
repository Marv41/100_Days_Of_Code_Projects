from tkinter import *
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

from Easy_Projects.hangman_game.hangman_words import word_list

BACKGROUND_COLOR = "#B1DDC6"
timer_ms = 3000
file = "data/french_words.csv"
language = "French"
to_learn = {}
current_card = {}

#import csv
try:
    df = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv(file)
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(card_word, text="END")
    else:
        canvas.itemconfig(card, image=card_front)
        canvas.itemconfig(card_title, text=language, fill="black")
        canvas.itemconfig(card_word, text=current_card[language], fill="black")
        flip_timer = window.after(timer_ms, flip_card)

def correct():
    to_learn.remove(current_card)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#GUI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(timer_ms, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, command=correct, highlightthickness=0)
right_button.grid(column=1, row=1)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))

#Start main function
next_card()


window.mainloop()