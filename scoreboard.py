from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score()
    
    def score(self):
        self.clear()
        self.goto(100, 140)
        self.write(self.right_score , font=("Courier", 40, "normal"), align="Center")
        self.goto(-100, 140)
        self.write(self.left_score , font=("Courier", 40, "normal"), align="Center")

    
    def winner(self, winner, placing, place):
        self.goto(place)
        self.write(winner,font=("Courier", 30, "normal"), align=placing )
