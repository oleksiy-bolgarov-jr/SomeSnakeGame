from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def eat(self):
        self.refresh()

    def refresh(self):
        x_pos = random.randrange(-260, 280, 20)
        y_pos = random.randrange(-260, 280, 20)
        self.goto(x_pos, y_pos)
