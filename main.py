from turtle import Screen, Turtle
from user_paddle import User_paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Make the main black screen with a dotted line in the center
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=400)
screen.bgcolor("black")

turtle = Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.goto(x=0,y=180)
turtle.setheading(270)
turtle.color("white")
turtle.pensize(5)
turtle.hideturtle()

for _ in range(18):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

# Make a moving paddle on the left
paddle_left = User_paddle((-380,0))
paddle_left.shape("square")
paddle_right = User_paddle((380,0))
paddle_right.shape("square")

screen.listen()
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)

ball = Ball()
ball.shape("circle")

scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.005)
    screen.update()
    ball.move()

    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.bounce()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 365 or ball.distance(paddle_left) < 50 and ball.xcor() < -365:
        ball.pad_bounce()
        ball.x_move *= 3

    elif ball.xcor() > 400:
        scoreboard.left_score += 1
        scoreboard.score()
        ball.goto(0,0)
        ball.x_move = 0.75
        ball.x_move *= -1

    elif ball.xcor() < -400:
        scoreboard.right_score += 1
        scoreboard.score()
        ball.goto(0,0)
        ball.x_move = 0.75
        ball.x_move *= -1
    
    if scoreboard.right_score == 5:
        scoreboard.winner(winner="THE\nPLAYER\nON\nTHE\nRIGHT\nWON", placing= "Left", place=(100,-100))
        game_is_on = False

    elif scoreboard.left_score == 5:
        scoreboard.winner(winner="THE\nPLAYER\nON\nTHE\nLEFT\nWON", placing= "Right", place=(-100,-100))
        game_is_on = False


















screen.exitonclick()