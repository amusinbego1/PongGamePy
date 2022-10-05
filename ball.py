from turtle import Turtle
from settings import X_DIMENSION, Y_DIMENSION, BLOCK_DIMENSION
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.setheading(randint(-70, -10))

    def move(self):
        self.forward(10)
        if self.ycor() >= Y_DIMENSION/2 - BLOCK_DIMENSION//2 or self.ycor() <= -Y_DIMENSION/2 + BLOCK_DIMENSION/2:
            self.setheading(-self.heading())

