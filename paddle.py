from turtle import Turtle
from settings import X_DIMENSION, Y_DIMENSION, BLOCK_DIMENSION


class Paddle(Turtle):
    def __init__(self, difficulty):
        super().__init__()
        if difficulty.lower() == "easy":
            self.len = 7
        elif difficulty.lower() == "hard":
            self.len = 3
        else:
            self.len = 5
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(self.len, 1)

    def move_up(self):
        if self.ycor() + BLOCK_DIMENSION*self.len//2 + BLOCK_DIMENSION <= Y_DIMENSION//2:
            self.goto(self.xcor(), self.ycor() + 25)

    def move_down(self):
        if self.ycor() - BLOCK_DIMENSION*self.len//2 - BLOCK_DIMENSION  >= -Y_DIMENSION//2:
            self.goto(self.xcor(), self.ycor() - 25)

    def is_close(self, ball):
        "prima loptu i poredi sa svakim dijelom reketa"
        for x in range(-self.len//2, self.len//2 + 1):
            if ball.distance(self.xcor(), self.ycor() + x*BLOCK_DIMENSION) <= 25:
                return True
        return False



