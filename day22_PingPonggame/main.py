from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
import time
from scorebord import Scorebord

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()
scorebord = Scorebord()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detection of collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.reflect()

    if ball.xcor()>360:
        ball.reset_positio()
        scorebord.l_point()

    if ball.xcor()<-360:
        ball.reset_positio()
        scorebord.r_point()

screen.exitonclick()
