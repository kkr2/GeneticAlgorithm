import turtle


class player(turtle.Turtle):
    def __init__(self,x,y,sh):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.color('red')
        self.shape(sh)





    def turnLeft(self):
        self.goto(self.xcor()-20,self.ycor())
    def turnRight(self):
        self.goto(self.xcor()+20,self.ycor())
    def up(self):
        self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        self.goto(self.xcor(),self.ycor()-20)
