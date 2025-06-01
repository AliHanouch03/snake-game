from turtle import Turtle

snake = Turtle()


class Snake:
    def __init__(self, shape, color, position):
        self.shape = shape
        self.color = color
        self.position = position