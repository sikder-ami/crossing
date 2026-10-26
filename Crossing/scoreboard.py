from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.goto(-230,250)
        self.write(f'LEVEL:{self.level}',align='center',font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,250)
        self.write(f'GAME OVER YOUR LEVEL IS {self.level}',align='center',font=FONT)

