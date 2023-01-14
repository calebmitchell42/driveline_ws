'''
Header: CS 122 Fall 2022 Project 7-1
Author: Caleb Mitchell
Credit: Worked with Benjamin DeWeese van Schooneveld
Description: 2 Functions to transcribe DNA to RNA using a for loop and a while loop
'''

import doctest

def transcribe1(s):
    '''
    Transcribe1` uses for loop to transcribe DNA to RNA
    
    >>> transcribe1('ACGT TGCA')
    'UGCAACGU'
    
    >>> transcribe1('GATTACA')
    'CUAAUGU'
    
    >>> transcribe1('GAtTtTACA')
    'CUAAUGU'
    
    >>> transcribe1('TTt ACT')
    'AAUGA'

    
    >>> transcribe1('cs5')
    ''
    '''
    RNA = ''                #sets RNA equal to a string
    
    for i in s:             #repeats for as many letters are in the string
        if i == 'A':
            RNA += 'U'      #adds U to the RNA string if I is in the parameter
        elif i == 'C':
            RNA += 'G'      #adds G to the RNA string if C is in the parameter
        elif i == 'G':      
            RNA += 'C'      #adds C to the RNA string if G is in the parameter
        elif i == 'T':      
            RNA += 'A'      #adds A to the RNA string if T is in the parameter
        else:
            RNA += ''       #adds nothing to the string if none of the letters are the parameter and capitalized

    return (RNA)            

def transcribe2(s):
    '''
    Transcirbe2 uses while loop to transcribe DNA to RNA
    
    >>> transcribe1('ACGT TGCA')
    'UGCAACGU'
    
    >>> transcribe1('GATTACA')
    'CUAAUGU'
    
    >>> transcribe1('GAtTtTACA')
    'CUAAUGU'
    
    >>> transcribe1('TTt ACT')
    'AAUGA'
    
    >>> transcribe1('cs5')
    ''
    '''
    RNA = ''                    #sets RNA equal to a string
    i = 0                       #makes i start at 0
    while (i <= len(s)):        #repeat while the i is less than or equal to the length of the string in the parameter
        if s[i:i+1] == 'A':     
            RNA += 'U'          #adds U to the string if the next letter in the string is A 
            i += 1
        elif s[i:i+1] == 'C':
            RNA += 'G'          #adds G to the string if the next letter in the string is C
            i += 1
        elif s[i:i+1] == 'G':
            RNA += 'C'          #adds C to the string if the next letter in the string is G
            i += 1
        elif s[i:i+1] == 'T':
            RNA += 'A'          #adds A to the string if the next letter in the string is T
            i += 1
        else:
            RNA += ''           #adds nothing to the string if the letter isn't in the parameter
            i += 1
            
    return (RNA)


print(doctest.testmod())        #tests the docstring

#i think that the for loop is a better choice since it requires less arguments and works with the length of the string that is input in the parameter

#end
