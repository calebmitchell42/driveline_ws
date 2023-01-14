
import math

def check_positive_int(n):
    if (n > 0):
        positive_int = True
    else:
        positive_int = False
    print(positive_int)
    return

def check_3_digits(n):
    if (n <1000 and n >= 100):
        three_digits = True
    else:
        three_digits = False
    print(three_digits)
    return

def check_end_digits(n):
    if (n % 10 != math.floor(n/100)):
        end_digits = True
    else:
        end_digits = False
    print(end_digits)
    return

def check_number(n):
    check1 = check_positive_int(n)
    check2 = check_3_digits(n)
    check3 = end_digits
    
    if (check1 and check2 and check3 == True):
        valid_number = True
    else:
        valid_number = False
    print(valid_number)

check_number(253)
