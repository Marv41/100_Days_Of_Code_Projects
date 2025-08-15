from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280.00


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("green")
        self.finish_line = FINISH_LINE_Y
        self.refresh()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.clear()
        self.goto(STARTING_POSITION)




