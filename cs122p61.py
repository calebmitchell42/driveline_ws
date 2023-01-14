'''
Title: CS 122 Fall 2022 Project 6-1 - Square Root
Author: Caleb Mitchell
Credits: Worked with Benjamin DeWeese van Schooneveld
Description: Function that calculates approximate square root and compares it to math.sqrt funciton
'''
import math

def mysqrt(a):
    '''
    Calculates the square root of a number using a while loop
    >>>myqrt(1)
    1
    '''
    x = 1
    epsilon = .0001
    while True:
        y = (x + a/x) / 2   #given equation to calculate square root'
        if y == x:      #tests if variables are equal to eachother'
            break
        elif (abs(y-x) <= epsilon):     #if the difference of the square root and the a value is less or equal to epsilon the function ends
            break
        x = y
    return x

def square_root_compare():
    '''
    callsmyqrt and compares the value it gets to math.sqrt and then calculates the difference
    >>>square_root_compare()
    a     mysqrt(a)         math.sqrt()     diff
    0     0.0001220703125   0.0             0.0001220703125
    '''
    for i in range(11):     #for loop that compares the square root 11 times starting at 0
        print(f'{i:<5}{mysqrt(i):<25}{math.sqrt(i):<25}{mysqrt(i)-math.sqrt(i):<25}')
 
    return


def main():
    '''driver for function and calls square root compare
    '''
    a = 1
# print table header
    print('\nSquare Root Calculator\n')
    print(f'{"a":5}{"mysqrt(a)":25}{"math.sqrt()":25}{"diff":25}')
    square_root_compare()       #calls the compare square root funciton
    return

main()  #calls main function

#end
        
    
