from turtle import Turtle

class Paddle(Turtle):
    
    #Creating the paddle object
    def __init__(self, position):
        super().__init__();
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)
    
    #Defining movement for up and down
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)