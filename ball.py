from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setposition(0,0)
        self.x_move = 0.75
        self.y_move = 0.75

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def bounce(self):
        self.y_move *= -1

    def pad_bounce(self):
        self.x_move *= -1

    
        