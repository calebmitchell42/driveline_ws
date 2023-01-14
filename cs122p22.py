'''
CS 122 Fall 2022 Project 2-2
Author(s): Caleb Mitchell, C. Science
Credit: Consulted with Benjamin DeWeese van Schoonedveld:
Python functions; minimum payment function
'''

import math

def payment(balance):
    '''
    Calculates the minimum payment for a credit card company based on
    different balances.

    >>> payment(balance)
    Minimum payment for balance $x is $y
    '''
    one = 10
    two = 0.021*balance
    total_1= max(one,two)
    total_2= round(min(total_1, balance))
    print(f'Minimum payment for balance $ {balance} is ${int(total_2)}')
    return

payment(1000)
payment(600)
payment(25)
payment(8)

#end#
