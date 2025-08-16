import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_direction = 10
        self.y_direction = -10

    def ball_reset(self):
        self.goto(0, 0)
        self.paddle_bounce()

    def move_ball(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x + self.x_direction, y + self.y_direction)

    def bounce(self):
        self.y_direction *= -1

    def paddle_bounce(self):
        self.x_direction *= -1


