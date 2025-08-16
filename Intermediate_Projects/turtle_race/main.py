import random
import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()

#Turn Right
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

#Dashed Line
# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.up()
#     my_turtle.forward(10)
#     my_turtle.down()

#Multiple Shapes
r = 0
g = 0
b = 0
turtle.colormode(255)
my_turtle.width(5)

for sides in range(3,11):
    angle = 360 / sides
    my_turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)






my_screen = Screen()
my_screen.exitonclick()








































