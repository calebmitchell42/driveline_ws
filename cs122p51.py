'''
Title: CS 122 Fall 2022 Project 5-1 - Mars rover
Author: Caleb Mitchell
Credits: Worked with Benjamin DeWeese van Schooneveld
Description: Mars rover that goes around and collects data points
'''

from turtle import *
import random

def rover_loc():
    '''
    Measures the rovers location at a random x,y between -275 and 275
    >>>rover_loc()
    (gets called in collect_data and prints data there)
    '''
    return random.randint(-275, 275)

def water_content():
    '''
    Measures the water content at a rovers location between 1 and 290
    >>>water_content()
    (gets called in collect_data and prints data there)
    '''
    return random.randint (1, 290)

def temperature():
    '''
    Measures the temperature at a rovers location between -178 and 1
    >>>temperature()
    (gets called in collect_data and prints data there)
    '''
    return random.randint (-178, 1)

def collect_data():
    '''
    Collects all of the temperature, location and water_content data
    >>>collect_data()
    (gets called in mars explore function)
    '''
    x = rover_loc()
    y = rover_loc()
    pendown()
    setposition(x, y)   #rover goes to the positoin called in rover_loc
    dot()
    temp = temperature() 
    water = water_content()
    print(x, '\t', y, '\t', temp,  '\t', '\t', water,)
    return 

def mars_explore(stops):
    '''
    set up to do the data collection multiple times
    >>>mars_explore(stops)
    (gets called in main function)
    '''
    for n in range (stops):
        collect_data()
    return

def mars_explore_setup():
    '''
    set up printed and graphical output called from: mars_explore_main
    >>> mars_explore_setup()
    '''
# print title line for printed output
    print('x', '\t', # label for print output
    'y', '\t', # note special char \t
    'water_content', '\t', # which acts like the
    'temperature') # tab key

                                                    
# set up graphical output
    reset()
    title('Mars Rover')
    speed('fastest')
    display_color = 'blue'
    pencolor(display_color)
    dot(10, display_color) #mark the rover's starting position

    return

def mars_explore_main():
    '''
    Calls all of the functions to collect the data and print it then repeat multiple times
    >>>mars_explore_main()
    x    y    water_content   temperature
    144  10     -47              148
    '''
    mars_explore_setup()    #calls the set up function
    mars_explore(20)        #calls for rover to collect 20 data points

    return
    
mars_explore_main()

#end
