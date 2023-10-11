from turtle import Turtle

class User_paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.speed("fastest")
        self.shapesize(stretch_len= 0.5,stretch_wid= 5)
        self.penup()
        self.color("white")
        
    
    def up(self):
        if self.ycor() < 150:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -150:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)