from my_screen import MyScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_on = True

# create screen object *new_screen*
screen = MyScreen()
new_screen = screen.create_new_screen()
screen.create_border_turtle()
scoreboard = Scoreboard()

#create paddle object *paddle*
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

#create ball
ball = Ball()
sleep_time = .1

while game_on:
    # scoreboard.update()
    time.sleep(sleep_time)
    new_screen.update()
    new_screen.listen()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.r_score += 1
        sleep_time -= .01
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.l_score += 1
        sleep_time -= .01

    scoreboard.update()



    new_screen.onkeypress(fun=r_paddle.move_up, key="Up")
    new_screen.onkeypress(fun=r_paddle.move_down, key="Down")
    new_screen.onkeypress(fun=l_paddle.move_up, key="w")
    new_screen.onkeypress(fun=l_paddle.move_down, key="s")

new_screen.mainloop()