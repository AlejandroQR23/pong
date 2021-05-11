
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

# * Screen
screen = Screen()
screen.setup( width=800, height=600 )
screen.title( "Pong" )
screen.bgcolor( "black" )
screen.tracer( 0 )

# * Scoreboard
scoreboard = Scoreboard()

# * Ball
ball = Ball()

# * Paddles
r_paddle = Paddle( xcor=350, ycor=0 )
l_paddle = Paddle( xcor=-350, ycor=0 )

# * Paddles controls
screen.listen()
screen.onkeypress( r_paddle.up, "Up" )
screen.onkeypress( r_paddle.down, "Down" )
screen.onkeypress( l_paddle.up, "w" )
screen.onkeypress( l_paddle.down, "s" )

# * Game flow
game_is_on = True
while game_is_on:
    time.sleep( ball.move_speed )
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')
    # Detect collision with the paddles
    elif ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce('x')
    # Detects if the ball bounds at the edge
    elif ball.xcor() > 380:
        scoreboard.increase_score( 'left' )
        ball.restart()
    elif ball.xcor() < -380:
        scoreboard.increase_score( 'right' )
        ball.restart()


screen.exitonclick()
