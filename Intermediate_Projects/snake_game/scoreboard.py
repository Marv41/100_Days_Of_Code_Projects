from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_scoreboard()


    def add_to_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\n   Score: {self.score} ", align="center", font=("Arial", 40, "normal"))

