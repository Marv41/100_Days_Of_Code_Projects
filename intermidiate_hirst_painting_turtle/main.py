import turtle as t
import random



###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
t.colormode(255)
screen = t.Screen()
screen.setworldcoordinates(-500,-500,500,500)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def teleport(x, y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()

def draw_border():
    timmy.width(5)
    timmy.color("black")
    teleport(-450, -450)
    for side in range(4):
        timmy.forward(900)
        timmy.left(90)

def draw_circle():
    timmy.color(random.choice(color_list))
    timmy.begin_fill()
    timmy.circle(20)
    timmy.end_fill()

timmy= t.Turtle()
timmy.speed("fastest")

starting_x = -405
starting_y = -425

# draw_border()
timmy.hideturtle()

for _ in range(10):
    for _ in range(10):
        teleport(starting_x, starting_y)
        timmy.dot(20,random.choice(color_list))
        starting_x += 70

    starting_x = -405
    starting_y += 70
    teleport(starting_x, starting_y)


timmy.hideturtle()
screen.exitonclick()