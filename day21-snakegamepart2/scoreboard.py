from turtle import Turtle
Alignment = "center"
Font = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align=Alignment, font=Font)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over \n Score {self.score}", align=Alignment, font=Font)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


