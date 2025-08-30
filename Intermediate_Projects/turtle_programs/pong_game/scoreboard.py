import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 180)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=("Courier", 80, "normal"))
