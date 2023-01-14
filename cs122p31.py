'''
CS 122 Fall 2022 Project 3-1
Author(s):  Caleb Mitchell, Economics, Data Science
Credit:  CS 122 Resources only
Description:  Intro
to Python Turtle Graphics45
'''

from turtle import *

def poly(num_sides,side_len,color):
    '''
    draws square and triangle of the house
    >>> poly(4,100,'pink')
    [turle draws 4 lines with length 100 and colors it pink]
    '''
    fillcolor(color)
    begin_fill()
    for x in range(num_sides): 
        lt(360 / num_sides) #defining directions to draw polygon
        fd(side_len) #moving turtle by given length when poly() is called

    end_fill()    
    return

def jump(x, y):
    '''aux function sets turtle position
    without leaving pen trail
    >>> jump(100, 100)
    [turtle positioned at 100, 100]
    '''
    penup()
    setposition(x, y)
    pendown()
    return

    
def house():
    '''
    runs poly function for the square and the triangle
    >>>house()
    [turtle draws square and triangle and fills the color in]
'''
    poly(4,100,'pink') #draws a polygon with 4 sides, 100 length and the color pink
    jump(0, 100)
    poly(3,100, 'light blue') #draws a poloygon with 3 sides, 100 length and color light blue
    jump(0, 100)
    return

#for challenge part

def sunshine(x,y):
    '''
    draw a sun at position x, y
    >>> sunshine(0, 0)
    [drawing of a sun in the center of the turtle canvas]
    '''
    jump(100,200)
    pencolor('orange') #defines color of sun
    begin_fill()
    num_rays = 50 #how many lines turtle will draw
    ray_len = 60 #how long those lines are
    for x in range (num_rays):
        fd(ray_len)
        jump(100,200)
        lt(360 / num_rays)

    end_fill()
    return

def main():
    '''driver for code to draw a house'''
    # set up turtle environment
    reset()
    title('Caleb\'s house')
    speed(0)
    hideturtle()
    house() # draw the house
    sunshine(500,200) #draws sun from challnege part
    
main() #draws house and sunshine

#end
