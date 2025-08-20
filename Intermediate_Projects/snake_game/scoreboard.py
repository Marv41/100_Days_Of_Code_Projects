from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as highscore:
            self.high_score = int(highscore.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_scoreboard()


    def add_to_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over\n   Score: {self.score} ", align="center", font=("Arial", 40, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
