from turtle import Turtle, Screen
import time

# Sets up the properties of our screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
x_values = [0, -20, -40]
snake_segments = []


# turn_left() function is to turn the snake to the left
def turn_left():
    snake_segments[0].left(90)


screen.tracer(0)  # A method to stop refreshing the screen until we decide to refresh it using the update() method
for i in range(3):  # sets up the body of the snake
    snake = Turtle(shape= 'square')
    snake.color('white')
    snake.penup()
    snake.goto(x=x_values[i], y=0)
    snake_segments.append(snake)

screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Each segment of the snake takes the place of the segment in front of it starting from the end of the snake and
    # excluding the head of the snake. This method makes it easier to turn the snake towards different directions by
    # only modifying the direction of the head.
    for j in range(len(snake_segments) - 1, 0, -1):
        # j ranges from the length of the segment minus 1 until 1 by one unit decrement step
        x_cor = snake_segments[j - 1].xcor()  # storing the x coordinate of the front snake segment in this variable
        y_cor = snake_segments[j - 1].ycor()  # storing the y coordinate of the front snake segment in this variable
        snake_segments[j].goto(x=x_cor, y=y_cor)  # take the targeted segment to the new position
    snake_segments[0].forward(20)  # Moves the head 20 pixels to the front
    screen.onkey(fun=turn_left, key='Left')  # when the left arrow is pressed the head is turned 90 degrees to the left

screen.exitonclick()
