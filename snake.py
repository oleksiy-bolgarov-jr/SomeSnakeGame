from turtle import Turtle
from typing import Tuple

from food import Food

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        x_pos = 0
        for i in range(3):
            self.add_segment((x_pos, 0))
            x_pos -= MOVE_DISTANCE

    @property
    def head(self):
        return self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def collided_with_food(self, food: Food):
        return self.head.distance(food) < 15

    def collided_with_wall(self):
        return abs(self.head.xcor()) > 280 or abs(self.head.ycor()) > 280

    def collided_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

        return False

    def add_segment(self, position: Tuple[int, int]):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment((self.segments[-1].pos()))
