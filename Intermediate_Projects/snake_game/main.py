from window import Window
from snake import Snake
from food import  Food
from scoreboard import Scoreboard
import time

game_running = True

#create window and listen
window = Window()
screen = window.create_new_screen()
window.create_border()
screen.listen()

#create starting snake
snake = Snake()

#create food pellets
food = Food()

#create scoreboard
scoreboard = Scoreboard()

while game_running:
    screen.update()
    time.sleep(.05)
    wall_collision = snake.check_wall_collision()
    self_collision = snake.check_self_collision()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_tail()
        scoreboard.add_to_score()

    if wall_collision or self_collision:
        game_running = False
    else:
        snake.move()

    screen.onkeypress(fun=snake.down, key="Down")
    screen.onkeypress(fun=snake.up, key="Up")
    screen.onkeypress(fun=snake.right, key="Right")
    screen.onkeypress(fun=snake.left, key="Left")

scoreboard.game_over()
screen.exitonclick()
