
import turtle
import math
import time
from random import uniform

class Player(turtle.Turtle):
    def __init__(self, x, y, speed):
        turtle.Turtle.__init__(self)
        self.color('black')
        self.shape('classic')
        self.speed = 100
        self.penup()
        self.setposition(x,y)


