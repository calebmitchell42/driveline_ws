'''
CS 122 Fall 2022 Project 3-2
Author(s):  Caleb Mitchell, Economics, Data Science
Credit:  CS 122 Resources only
Description:  Intro to Python Turtle Graphics
'''

from turtle import *

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

def sunshine(x,y):
    '''
    draw a sun at position x, y
    >>> sunshine(0, 0)
    [drawing of a sun in the center of the turtle canvas]
    '''
    pencolor('orange')
    begin_fill()
    num_rays = 50 #defines number of lines to draw
    ray_len = 60 
    for x in range (num_rays): #code that draws sun
        fd(ray_len)
        jump(0,0)
        lt(360 / num_rays) #360 degrees so drawing is a circle

    end_fill()
    return

def main():
    '''driver for code to draw a sun
    >>> main()
    [Draws orange sun in middle of canvas]
    '''
    # set up turtle environment
    reset()
    title('Caleb Mitchell Star')
    speed('fastest')
    hideturtle()
    # draw the sun
    sunshine(0, 0)
    return

main() #draws sun

#end
