from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 19, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear() # clears the scoreboard
        self.score += 1 # increments the score when a collision of the head with the circle-turtle is detected
        self.update_scoreboard()

