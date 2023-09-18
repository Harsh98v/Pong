from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

#Setting up the screen
sc = Screen()
sc.bgcolor("black")
sc.screensize(800, 600)
sc.title("Pong")
sc.tracer(0)

#Creating the left and right paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

#Creating the ball
ball = Ball()

#Creating the score tracker
score = Score()

#Listening to the screen for keyboard inputs
sc.listen()

#Controls for right paddle
sc.onkey(right_paddle.go_up, "Up")
sc.onkey(right_paddle.go_down, "Down")

#Controls for left paddle
sc.onkey(left_paddle.go_up, "w")
sc.onkey(left_paddle.go_down, "s")

#To decide how long the game should be running
game_running = True

while game_running:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    
    #Detect collision with the wall
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()
        
    #Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #increase speed of the ball after every hit

    #Right side paddle miss
    if ball.xcor() > 380:
        #Reset position of the ball back to the center
        ball.reset_position()
        #Update the score
        score.update_left()
    
    #Left side paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_right()
    
sc.exitonclick()