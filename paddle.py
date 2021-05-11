
from turtle import Turtle

class Paddle( Turtle ):

    def __init__( self, xcor, ycor ):
        super().__init__()
        self.penup()
        self.color( "white" )
        self.shape( "square" )
        self.shapesize( stretch_wid=5, stretch_len=1 )
        self.goto( x=xcor, y=ycor )

    def up( self ):
        self.goto( self.xcor(), self.ycor()+20 )

    def down( self ):
        self.goto( self.xcor(), self.ycor()-20 )