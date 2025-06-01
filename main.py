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

# turn_left() function is to turn the snake to the left
def turn_left():
    snake.segments[0].left(90)

screen.tracer(0)  # A method to stop refreshing the screen until we decide to refresh it using the update() method

screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(fun=turn_left, key='Left')  # when the left arrow is pressed the head is turned 90 degrees to the left

screen.exitonclick()
