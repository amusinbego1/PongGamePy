from turtle import Turtle, Screen
from paddle import Paddle
from settings import X_DIMENSION, Y_DIMENSION, BLOCK_DIMENSION
from ball import Ball
from time import sleep
from score import Score


screen = Screen()
screen.setup(X_DIMENSION, Y_DIMENSION)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


difficulty = screen.textinput("Difficulty", "Choose difficulty ('hard', 'normal', 'easy'): ")
ZA_POBJEDU = screen.numinput("", "Do koliko se igra: ", 5, 1)
lefty = screen.textinput("Player on the left", "Insert name of lefty")
righty = screen.textinput("Player on the right", "Insert name of righty")

dashed = Turtle()
dashed.speed("fastest")
dashed.hideturtle()
dashed.color("white")
dashed.penup()
dashed.goto(0, -Y_DIMENSION/2 - 20)
dashed.setheading(90)
for i in range(int(-Y_DIMENSION/2 - 10), int(Y_DIMENSION + 10), 10):
    dashed.pendown()
    dashed.forward(5)
    dashed.penup()
    dashed.forward(7)
screen.update()

right_p = Paddle(difficulty)
right_p.goto(X_DIMENSION//2 -BLOCK_DIMENSION  -10, 0)
left_p = Paddle(difficulty)
left_p.goto(-X_DIMENSION//2 +BLOCK_DIMENSION +10, 0)
screen.update()
screen.listen()
screen.onkey(right_p.move_up, "Up")
screen.onkey(right_p.move_down, "Down")
screen.onkey(left_p.move_up, "w")
screen.onkey(left_p.move_down, "s")
ball = Ball()
speed = 0.05

left_score = Score()
left_score.goto(-50, Y_DIMENSION/2 - 70)
left_score.pisi()
right_score = Score()
right_score.goto(50, Y_DIMENSION/2 - 70)
right_score.pisi()


def update(score):
    global speed
    speed = 0.05
    score.score += 1
    score.pisi()
    sleep(1)
    ball.goto(0, 0)


should_continue = True
while should_continue:
    if right_p.is_close(ball) or left_p.is_close(ball):
        ball.setheading(180 - ball.heading())
    if ball.xcor() > X_DIMENSION/2 + BLOCK_DIMENSION*2:
        update(left_score)
    elif ball.xcor() < -X_DIMENSION/2 - BLOCK_DIMENSION*2:
        update(right_score)
    ball.move()
    screen.update()
    sleep(speed)
    if speed - 0.00004 > 0:
        speed -= 0.00003
    if left_score.score == ZA_POBJEDU:
        winner = lefty
        should_continue = False
    elif right_score.score == ZA_POBJEDU:
        winner = righty
        should_continue = False

cong = Turtle()
cong.hideturtle()
cong.penup()
cong.color("Yellow")
ball.hideturtle()
dashed.clear()
screen.update()
cong.write(f"The winner is {winner}", False, "center", ("Courier", 25, "normal"))
screen.exitonclick()