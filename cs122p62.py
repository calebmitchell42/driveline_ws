'''
Title: CS 122 Fall 2022 Project 6-2 - Rock Paper Scissors
Author: Caleb Mitchell
Credits: Worked with Benjamin DeWeese van Schooneveld
Description: Function plays rock paper scissors until there is a winner
'''

import random

rock = 1    #sets rocks value to 1
paper = 2   #sets papers value to 2
scissors = 3  #sets scissors values to 3


def rps():
    '''
    Plays rock paper scissors until there is a winner and then finds who the winner is
    >>>rps()
    side 1 wins! (if side 1 throws rock and side 2 scissors)
    '''
    winner = True       #winner is set equal to true
    
    while True:     #while winner is true the function will run once if not it will run until there is a winner
        side1 = random.randint(1,3)     #side 1 is assigned a random int 1-3
        side2 = random.randint(1,3)     #side 2 is assigned a random int 1-3
        print(side1, side2)     #prints what each side throws
        
        if side1 == rock and side2 == scissors:
            print('side 1 wins!')
            winner = True
            break
        
        elif side1 == rock and side2 == paper:
            print('side 2 wins!')
            winner = True
            break
        
        elif side1 == scissors and side2 == rock:
            print('side 2 wins!')
            winner = True
            break
        
        elif side1 == scissors and side2 == paper:
            print('side 1 wins!')
            winner = True
            break
        
        elif side1 == paper and side2 == rock:
            print('side 1 wins!')
            winner = True  
            break
        
        elif side1 == paper and side2 == scissors:
            print('side 2 wins!')
            winner = True
            break
        
        elif side1 == side2:        #if the two sides throw the same thing its a tie and there is not winner 
            print('This is a tie')
            winner = False
                 
    return

rps()   #calls rps function

#end
