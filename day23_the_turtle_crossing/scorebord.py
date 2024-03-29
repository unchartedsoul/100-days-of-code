from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_scorebord()

    def update_scorebord(self):
        self.clear()
        self.write(f"level {self.level}", align="left", font=FONT)


    def incres_level(self):
        self.level+=1
        self.update_scorebord()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center",font=FONT)
