import Turtle as t
playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("green")
window.setup(width = 800, height = 600)
window.tracer(0)

#Left paddle
leftpaddle = t.Turtle(0)
leftpaddle.speed(0)
leftpaddle.shape("Square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

#Right paddle
Rightpaddle = t.Turtle(0)
Rightpaddle.speed(0)
Rightpaddle.shape("Square")
Rightpaddle.color("white")
Rightpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
Rightpaddle.penup()
Rightpaddle.goto(350, 0)

#Ball

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.2
ballydirection = 0.2

#Score

pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write ("score", align = "center", font = ('Arial', 24, 'normal'))

#moving leftpaddle

def leftpaddleup():
    y = leftpaddle.ycor()
    Y = Y + 90
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    Y = Y - 90
    leftpaddle.sety(y)

#moving rightpaddle

def rightpaddleup():
    y = leftpaddle.ycor()
    Y = Y + 90
    rightpaddle.sety(y)

def rightpaddledown():
    y = leftpaddle.ycor()
    Y = Y - 90
    rightpaddle.sety(y)

#playing keys

window.listen()
window.onkeypress(leftpaddleup, 'W')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up' )
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    #ball moving
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection*-1
    if ball.ycor() > -290:
        ball.sety(-290)
        ballydirection = ballydirection*-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection = ballxdirection
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("player A:{} player B:{}" .format(playerAscore,playerBscore), align = 'center', font = ('Arial', 24, 'normal'))


#collision

if (ball.xcor()>340)and(ball.xcor<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()rightpaddle.ycor()-40)
    ball.setx(340)
    ballxdirection = ballxdirection*-1

if (ball.xcor()>340)and(ball.xcor<350)and(ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()leftpaddle.ycor()-40)
    ball.setx(-340)
    ballxdirection = ballxdirection*-1
