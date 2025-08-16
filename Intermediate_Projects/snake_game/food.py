import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5)
        self.speed("fastest")
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250,250), random.randint(-280,250))