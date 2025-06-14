from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Sets up the properties of our screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

# create a snake
snake = Snake()

# create the food
food = Food()

# create scoreboard
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # updates the needed parameters namely:
        food.refresh() # position of the food
        snake.extend() # length of the snake
        scoreboard.increase_score() # scoreboard

    # Detect collision with wall
    if snake.head.xcor() < -296 or snake.head.xcor() > 296 or snake.head.ycor() < -296 or snake.head.ycor() > 270:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if the head collides with any segment in the tail:
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
