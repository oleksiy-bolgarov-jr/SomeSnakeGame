from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 280)

        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("YOU'RE DEAD", align=ALIGNMENT, font = FONT)
