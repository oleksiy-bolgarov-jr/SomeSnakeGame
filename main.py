from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.collided_with_food(food):
        food.eat()
        snake.extend()
        scoreboard.increment_score()

    if snake.collided_with_wall() or snake.collided_with_tail():
        scoreboard.game_over()
        break

screen.exitonclick()
