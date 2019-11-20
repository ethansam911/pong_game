#Pong game
#turtle module getting started with games
import turtle
import os

#Screen capitalized
win = turtle.Screen()
win.title("Pong by Ethan")

win.bgcolor("black")

win.setup(width=800, height=600)
#Stops window from updating
win.tracer(0)

#0 0 is at the center
#-300 down, -400 left, +400 right, +300 up

#Main game loop
#Can't mix spaces and tabs
#This doesnt use OOP because its for beginners
#And this is my refresher
#Pygame is good for full-fledged games but turtles are better for beginners


# Paddle A
#Capital T for class name
#lowercase t for module turtle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)


#Let's make the ball!
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
#X Y coordinates
ball.goto(0, 0)

#Moves by two pixels
ball.dx = 0.2
ball.dy = -0.2

#Paddle A functionality!
#Function - One piece at a time
def paddle_a_up():
    y = paddle_a.ycor()
    #Add 20 pixels
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    #Subtract 20 pixels
    y -= 20
    paddle_a.sety(y)

#Paddle B functionality!
def paddle_b_up():
    y = paddle_b.ycor()
    #Add 20 pixels
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    #Subtract 20 pixels
    y -= 20
    paddle_b.sety(y)

# Keyboard  bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

#Old school programming methodology
#Main game while loop
#Tabs and spaces matter!
while True:
    win.update()

#Move the ball
#Current position plus the change
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking Ceiling
    if ball.ycor() > 290:
        ball.sety(290)
        #This reverses the direction
        ball.dy *= -1

    #Border checking Floor
    if ball.ycor() < -290:
        ball.sety(-290)
        #This reverses the direction
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

# Paddle and ball collisions
# This should be 10 pixels before the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        #Moves the ball to the left a bit
        ball.setx(340)
        ball.dx *=-1