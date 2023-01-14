'''
CS 122 Fall 2022 Project 5-2
Author(s):  Caleb Mitchell
Credit: Worked with Benjamin DeWeese van Schooneveld
Description: Einstein math trick
'''
import math

def main():
    '''driver for einstein program'''
    # magic_number = 1089: the number is never refrenced so I'm not sure why it's here
    n = input('Enter a 3-digit positive number (different 1st and last digits): ')
    n = int(n)
    valid_number = check_number(n)
    if (valid_number == False):     #if the number fails any of the checks the program prints number is invalid and doesn't run
        print("Number is invalid")
    else:
        einstein(n)     #if the number passes all the checks then the program runs
    return
    '''
    >>>main()
    Enter a 3-digit positive number (different 1st and last digits): 325
    number is 325
    reverse is, 523
    difference is, 198
    the reverse is, 891
    magic number is... 1089
    '''

def check_positive_int(n):
    '''
    Checks to see if the user input is a positive statement
    
    >>>check_positive_int(n) #where n> 0
    >>> True
    '''
    if (n > 0):     #if n is greater then 0 then it must be positive
        positive_int = True
    else:
        positive_int = False
    return positive_int

def check_3_digits(n):
    '''
    Checks to see if the user input has three digits

    check_3_digits(n) #where n has 3 digits
    >>> True
    '''
    if (n < 1000 and n > 99):   #if n is greater then 99 and smaller then 1000 and an int then it must have three digits
        three_digits = True
    else:
        three_digits = False
    return three_digits

def check_end_digits(n):
     '''
    Checks to see if the left and right digits are different
    
    >>>check_end_digits(n) #if the left and right digits are different 
    >>> True
    '''
     if (n % 10 != math.floor(n/100)):      #calculates that end digits are different
        end_digits = True
     else:
        end_digits = False
     return end_digits

def check_number(n):
    '''
    Runs all of the other checks to make sure that they are all true
    and the number is vaild for the einstein part

    >>>check_number(n) # where all of the checks are true
    valid_number = True
    '''
    check1 = check_positive_int(n)
    check2 = check_3_digits(n)
    check3 = check_end_digits(n)
    
    if ((check1 == True) and (check2 == True) and (check3 == True)):  #if all of the checks are true then the number is valid
        valid_number = True
    else:
        valid_number = False    #if any of them are false then the number is invalid
        
    return valid_number

def reverse(n):
    '''
    Switches the first and last numbers of the three digit number

    >>>reverse(n)
    (switches the first and lasts digits)
    '''
    n_1 = math.floor(n / 100)   #isolates the first digit
    n_2 = (math.floor(n/10) % 10) * 10   #isolates the second digit
    n_3 = ((n % 10) * 100)     #isolates the third digit 
    reverse = (n_3 + n_2 + n_1)     #adds the numbers to get the new reversed value
    return reverse

def einstein(n):    #Benjamin DeWeese van Schooneveld helped me with this function
    '''
    This funciton does all of the caluclations to find the magic number
    >>> einstein
    (is only called in the main function)
    '''
    difference = abs(n - reverse(n))
    print("original number is", n)      #prints user input
    print("reverse is,", reverse(n))    #reverses the number
    print("difference is,", difference)     #calculates the difference: n - reverse
    print("the reverse  of that isis,", reverse(difference))    #calculates the difference of the reverse
    print("magic number is...", (difference + reverse(difference)))     #calculates the difference plus the reverse difference
    return

main()

#end
