import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
# tim.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color_tuple = (r, g, b)
    return random_color_tuple

direction = {"east" : 0,
             "north" : 90,
             "west" : 180,
             "south" : 270,
}

#Draw a Random Walk
# for _ in range(100):
#     tim.width(10)
#     tim.speed("fast")
#     tim.color(random_color())
#     tim.setheading(random.choice(list(direction.values())))
#     tim.forward(40)

#Draw Spirograph
# current_heading = tim.heading()
# for _ in range(120):
#     tim.color(random_color())
#     tim.speed("fastest")
#     tim.circle(100)
#     print(tim.heading())
#     tim.setheading(current_heading)
#     current_heading += 3




s = Screen()
s.exitonclick()