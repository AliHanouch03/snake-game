from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:  # sets up the body of the snake
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def turn_left(self):
        self.segments[0].left(90)

    def move(self):
        # Each segment of the snake takes the place of the segment in front of it starting from the end of the snake and
        # excluding the head of the snake. This approach makes it easier to turn the snake towards different directions by
        # only modifying the direction of the head.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # seg_num ranges from the length of the segment minus 1 until 1 by one unit decrement step
            x_cor = self.segments[seg_num - 1].xcor()  # storing the x coordinate of the front snake segment in this variable
            y_cor = self.segments[seg_num - 1].ycor()  # storing the y coordinate of the front snake segment in this variable
            self.segments[seg_num].goto(x=x_cor, y=y_cor)  # take the targeted segment to the new position
        self.segments[0].forward(MOVE_DISTANCE)  # Moves the head 20 pixels to the front




