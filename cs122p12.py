'''
CS 122 Fall 2022 Project 1-2
Author: Caleb Mitchell, C. Science
Credit:
Description: Calculate number of watermelons needed for reunion
    '''

# Initialize variables with values

n_people = 50

n_adult = 35

n_child = 15

# Calculate number of watermelon slices needed

adult_slices = n_adult * 2

child_slices = (n_child * 3) * 1.1 #1.1 calculates the 10% extra#

total_slices_needed = adult_slices + child_slices

# Calculate number of watermelons needed (this may be a float)

w_slices = 10 #slices per watermelon#

total_w = total_slices_needed / w_slices

# Round the number of watermelons

total_w= round(total_w)

# Report total number of watermelons to buy

print(total_w, 'total number of watermelons needed')

#end#

