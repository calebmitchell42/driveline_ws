'''
CS 122 Fall 2022 Project 2-1
Author(s): Caleb Mitchell, C. Science
Credit: Consulted with Benjamin DeWeese van Schooneveld:
Description: Python functions; transportation problems.
'''

#Original Route#

def max_trans1(a, b, c):
    '''
    Calculates the maximum weight a truck can take through route
    a, b and c.

    >>> max_trans1
    Maximum weight for route 1: x
    '''
    max_trans1= min(a,b,c)
    print("Maximum weight for route 1:",max_trans1)
    return

max_trans1(1, 2, 3)
max_trans1(9, 6, 3)
max_trans1(0, 0, 0)

#Both Routes#

def max_trans2(a,b,c,d,e):
    '''
    Calculates the maximum weight a truck can take through route
    a, b, c or d, e. 

    >>> max_trans1
    Maximum weight of route 1 or route 2: x
    '''
     
    route1= min(a,b,c)
    route2= min(d,e)
    max_trans= max(route1, route2)
    print("Maximum weight of route 1 or route 2:",max_trans)
    return
    
max_trans2(1, 2, 3, 4, 5)
max_trans2(222, 110, 411, 54, 73)
max_trans2(0, 0, 0, 0, 0)

#end#
