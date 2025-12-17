from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x= 0, y= 280)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font=("Arial", 24, "normal"))