'''
Project: p1_turtle
Author: Caleb Mitchell
Description: A program using turtle to draw a duck
'''


from turtle import *        # imports the turtle module to the project

def body():
    '''
    Function draws the outline of a duck's body and fills it in yellow
    >>>body()
    Draws a series of lines that looks like a ducks body and fills it in yellow
    '''
    speed('fast')           # sets the turtle to draw quicker (repeated throughout)
    fillcolor('yellow')     # makes the shape be filled in yellow
    begin_fill()
    circle(100,120)         # draws first large circle
    print(pos())
    rt(120)                 # the series of turns and moves forward draw the duck
    fd(45)
    lt(90)
    fd(20)
    lt(90)
    fd(25)
    rt(90)
    circle(80,120)          # draws the head shape
    lt(15)
    fd(100)
    circle(100,150)         # draws the back of the body
    print(position())
    end_fill()
    return

def beak():
    '''
    Function that draws the beak and fills it in orange
    >>>beak()
    Draws the beak and fills it in orange
    '''
    penup()
    fillcolor('orange')           # chooses the beak color orange
    begin_fill()
    setpos(86.60,150)
    pendown()
    setheading(0)                 # the series of turns and moves forward draw the duck
    fd(45)
    lt(90)
    fd(20)
    lt(90)
    fd(45)
    lt(90)
    fd(20)
    end_fill()
    return

def legs():
    '''
    Funciton that draws the legs for the duck
    >>>legs()
    Draws the legs
    '''
    speed('fast')

    penup()
    setpos(12.48,1.27) 
    width(10)               # makes drawing wider
    pendown()

    setheading(270)         # tells turtle to go straight down
    fd(50)
    lt(90)
    fd(20)
    penup()
    setpos(-20,2)           # sets the postion back to -20x 2y
    setheading(270)         # tells turtle to go straight down
    pendown()
    fd(45)
    lt(90)
    fd(20)
    return

def eye():
    '''
    Function to draw the eye of a duck and fill it in black
    >>>eye()
    Draws a circle and fills it in black
    '''
    width(1)            # returns width to normal
    speed('fast')
    penup()             # this group of code makes sure there isn't
    setpos(50,180)      # a line that shows up when turtule moves to 
    pendown()           # draw the circle

    fillcolor('black')  # fills the circle black
    begin_fill()
    circle(15)          # draws the circle with radius 15
    end_fill()          # ends fill
    exitonclick()       # makes it not close until the window is clicked
    return
    
def duck():
    '''
    Calls all components of drawing the duck
    >>>duck()
    # calls body(), beak(), legs() and eye() function that draw the duck
    '''
    body()              # calls body funciton
    beak()              # calls beak funciton
    legs()              # calls legs function
    eye()               # calls eye function
    return

duck()                  # calls the duck function to draw the duck


#end of project#