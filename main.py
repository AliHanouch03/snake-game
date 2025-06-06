from turtle import Screen
from snake import Snake
import time

# Sets up the properties of our screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
snake_segments = []

# create a snake
snake = Snake()

#Control the snake
screen.listen() # Listening
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.tracer(0)  # A method to stop refreshing the screen until we decide to refresh it using the update() method

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
