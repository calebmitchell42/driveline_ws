'''
CS 122 Fall 2022 Project 7-2

TESTING AND DEBUGGING
STARTER CODE

Author: Caleb Mitchell

Credits: Worked with Benjamin DeWeese van Schooneveld
'''
import doctest

####
#(1) RAT WEIGHT
#### 
def rats(weight, p):
    '''(weight: float, p: float) -> None

    Print number of weeks it will
    take for a rat to weigh 2 times
    as much as its original weight
    (weight) if it gains weight at
    rate p percent per week.

    >>> rats(10, 10)
    The rat weighs 21.4 after 8 weeks.
    '''
    weeks = 0
    rate = p * .01
    
    weight2 = weight    #created new variable, weight2 and assigned it to weight
    
    while weight2 < (2 * weight):   #added colon 
        weight2 += weight2 * rate   #weight set to weight2
        weeks = weeks + 1           #changed wks to weeks so error is fixed

        
    weight = round(weight2, 1)      #changed weight to weight2
    print(f'The rat weighs {weight} after {weeks} weeks.')
    return

####
#(2) MINUTES TO YEARS
####
def minutesToHours(minutes):
    '''(minutes: number) -> float

    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60       
    #hours = round(hours, 2)    #this statement does nothing so I commeneted it out 
    #print(hours)               #that would lead to an error  
    return hours                #added hours              
    
def hoursToDays(hours):
    '''(hours: int) -> float

    convert input hours to days;
    return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    '''
    days = hours / 24
    days = round(days, 2)       #added so it rounds to two decimals
    return days

def daysToYears(days):
    '''(days: int) -> float

    convert input days to yearss;
    return years

    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''                     
    #days = 365             if its 365 then user input doesn't matter so commented it out
    years = days / 365    
    years = round(years, 2) 
    return years

def minutesToYears(m):
    '''(m: int) -> float

    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step

    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    '''
    h = minutesToHours(m)   #assigned minutes to hours to h
    d = hoursToDays(h)      #assigned hours to days to d 
    y = daysToYears(d)      #assigned days to years to y

    return y

####
#(3) COUNTING VOWELS
#### 
def count_vowels(s):
    '''(s: str) -> int

    Return number of vowels in s.

    >>> count_vowels('The quick brown fox')
    5
    >>> count_vowels('University of Oregon')
    8
    >>> count_vowels('Hello World')
    3
    >>> count_vowels('HELLO WORLD')
    3
    >>> count_vowels('Python')
    1
    >>> count_vowels('CCC')
    0
    
    more examples of use/test cases go here
    '''
    vowels = 'aeiouAEIOU'   #added capital letters as well
    ctr = 0
    
    for ch in s:
        if ch in vowels:    
            ctr += 1    #changed counter to ctr to fix error

    return ctr   #moved the return statement outside of for loop

####
#(4) REVERSE? (TEXT CH. 8)
#### 
def is_reverse(word1, word2):
    '''(word1: str, word2: str) -> bool

    compare two words and return True if
    one is the reverse of the other;
    case matters

    >>> is_reverse('abc', 'cba')
    True
    >>> is_reverse('abc', 'CBA')
    False
    >>> is_reverse('a', 'a')
    True
    >>> is_reverse('abcc', 'abcc')
    False
    >>> is_reverse('yes', 'no')
    False
    >>> is_reverse('abb', 'bbb')
    False
    >>> is_reverse('abc', 'zba')
    False
    '''
    if len(word1) != len(word2):
        return False 

    i = 0
    j = len(word2) 

    while j >= 0:           #made it greater than or equal to so that function also tests the 0 value of the index
        if word1[::] == word2[::-1]:    #if the index values read from 0 to the end match the index values read from the negative direction then the string is reversed
            return True
        else:                           #else the string is not reversed
            return False
    return True


print(doctest.testmod())

#end
