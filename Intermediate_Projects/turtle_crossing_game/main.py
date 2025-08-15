import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#create turtle
turtle = Player()

#create scoreboard
scoreboard = Scoreboard()

#create car
car_manager = CarManager()

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.car_list:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() >= turtle.finish_line:
        turtle.refresh()
        scoreboard.increase_level()
        scoreboard.update()
        car_manager.increase_speed()

    loop_count += 1
    screen.onkeypress(fun=turtle.move, key="Up")

screen.mainloop()
