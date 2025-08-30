import turtle
BORDER_GAP = 30
DASH_SIZE = 20

class MyScreen:
    def __init__(self):
        self.title = "Pong"
        self.background_color = "black"
        self.border_color = "white"
        self.speed = "fastest"
        self.size = [800, 600]

    def create_new_screen(self):
        screen = turtle.Screen()
        screen.setup(self.size[0], self.size[1])
        screen.title(self.title)
        screen.bgcolor(self.background_color)
        screen.tracer(0)
        return screen

    def create_border_turtle(self):
        border = turtle.Turtle()
        border.hideturtle()
        border.penup()
        border.speed(self.speed)
        border.color(self.border_color)
        border.goto(self.size[0] / 2 , self.size[1] / 2)
        border.setheading(180)
        self.draw_border(border)
        self.draw_dashed_line(border)

    def draw_border(self,border_turtle):
        for _ in range(2):
            border_turtle.pensize(10)
            border_turtle.pendown()
            border_turtle.forward(self.size[0])
            border_turtle.left(90)
            border_turtle.forward(self.size[1])
            border_turtle.left(90)
        border_turtle.penup()

    def draw_dashed_line(self, border_turtle):
        border_turtle.pensize(2)
        border_turtle.goto(0, self.size[1] / 2)
        border_turtle.setheading(270)
        while border_turtle.ycor() > -self.size[1] / 2:
            border_turtle.forward(DASH_SIZE)
            border_turtle.pendown()
            if border_turtle.ycor() > -self.size[1] / 2:
                border_turtle.forward(DASH_SIZE)
                border_turtle.penup()