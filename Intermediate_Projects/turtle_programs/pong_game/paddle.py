import turtle

class Paddle(turtle.Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.paddle_list = []
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.move_to_start(coordinate)

    def move_to_start(self,coordinate):
        self.clear()
        self.setx(coordinate)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 30)

    def move_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 30)