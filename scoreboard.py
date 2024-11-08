from turtle import Turtle

class Score(Turtle):
    def __init__(self):

        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score={self.score}",align="center", font=("Times New Roman", 24, "normal"))


    def update_scoreboard(self):
        self.score+=1
        self.clear()
        self.write(f"Score={self.score}", align="center", font=("Times New Roman", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
