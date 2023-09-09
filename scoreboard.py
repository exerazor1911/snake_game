from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.sety(270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ('Arial', 18, 'normal'))