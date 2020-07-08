import turtle

#Title of Canvas
turtle.title("Good Game")
#Background Color
turtle.bgcolor("green")
#setup
turtle.setup(700,700)
#Shape
turtle.shape("arrow")

#set up screen 
screen=turtle.Screen()

Alan=turtle.Turtle()

def rectangle(length):
 Alan.fillcolor("blue")
 Alan.begin_fill()
 x=0
 while x < 4:
   Alan.forward(length)
   Alan.right(90)
   x += 1 
   Alan.end_fill()
 
 #move forward by length 
 #turn 90 degrees 
 #How to move the turtle

 rectangle(200)