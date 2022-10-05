from turtle import Turtle
from settings import X_DIMENSION, Y_DIMENSION, BLOCK_DIMENSION


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pisi()

    def pisi(self):
        self.clear()
        self.write(f"{self.score}", False, "center", ("Courier", 40, "bold"))




