import turtle as tm

class Window:
    def __init__(self):
        self.width = 700
        self.height = 700
        self.background_color = "black"
        self.title = "My Snake Game"
        self.color = "white"

    def create_new_screen(self):
        screen = tm.Screen()
        screen.setup(self.width, self.height)
        screen.bgcolor(self.background_color)
        screen.title(self.title)
        screen.tracer(0)
        return screen

    def write_results(self,score):
        message = tm.Turtle()
        message.hideturtle()
        message.penup()
        message.color(self.color)
        message.goto(0,0)
        message.write(f"GAME OVER\n    Score: {score}", align="center",font=("Arial", 40, "normal"))
        return message

    def create_border(self):
        border = tm.Turtle()
        border.hideturtle()
        border.penup()
        border.goto(-300,-300)
        border.color(self.color)
        border.pensize(2)
        border.pendown()
        for side in range(4):
            border.forward(600)
            border.left(90)