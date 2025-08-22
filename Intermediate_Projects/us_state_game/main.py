import pandas
from turtle import Turtle,Screen

score = 0
exit_ = False
FONT = ('Arial', 8, 'normal')

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.setup(width=725,height=491)
screen.title("Name the States")

list_of_guesses = []
missing_states = []

data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

while score < 51 :
    guessed_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    if guessed_state == "Exit":
        missing_states = [state for state in list_of_states if state not in list_of_guesses]
        print(list_of_guesses)
        # print(missing_states)
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break

    if guessed_state in list_of_states:
        list_of_guesses.append(guessed_state)
        x_cor = data[data.state == guessed_state].x.item()
        y_cor = data[data.state == guessed_state].y.item()
        label = Turtle()
        label.penup()
        label.hideturtle()
        label.goto(x_cor,y_cor)
        label.write(f"{guessed_state}", align="center", font=FONT)
        score += 1




