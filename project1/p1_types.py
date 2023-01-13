'''
Project: p1_types
Author: Caleb Mitchell
Description: A program to demonstrate python's use of floating points
Credit: Python 3 documentation (15. Floating point arithmetic: issues and limitations)
'''


#1. Associative Property of Mulitplication

a = 10.0
b = 0.2
c = 0.4

# expected value should be true since there is the associate property
print(a * (b*c) == (b*a) * c)


#2. This doesn't work because python rounds the last digit

a = 1
b = .6

# expected value is 1.6 repeating
print(a/b)


#3. This is false because 3 goes to infinity so this is just an aproximiation
# which could be important when the calculation must be very percise

a = 3/9
b = 1

# expected value is 1.3 repeating
print(a*b)


#4. The 0.1 Problem: the issue arises in the way that 0.1 is stored in binary

a = 0.1
b = 0.2

# expeted value is 0.3
print(a+b == 0.3)


#5. Multiplying with 0.1: same issue

a = 0.1
b = 0.2

# expected value is 0.02
print(a*b == 0.02)


#end