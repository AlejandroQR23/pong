
from turtle import Turtle

class Ball( Turtle ):

    def __init__( self ):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

        self.x_dir = 10
        self.y_dir = 10
        self.move_speed = 0.1

    def move( self ):
        self.goto( self.xcor()+self.x_dir, self.ycor()+self.y_dir )
    
    def bounce( self, dir ):
        if dir == 'y':
            self.y_dir *= -1
        elif dir == 'x':
            self.x_dir *= -1
            self.move_speed *= 0.9 

    def restart( self ):
        self.bounce('x')
        self.move_speed = 0.1
        self.home()