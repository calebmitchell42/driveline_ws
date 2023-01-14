'''
CS 122 Fall 2022 Project 1-1
Author: Caleb Mitchell, C. Science
Credit: 
Description: Hello, Python - intro problems and code
    '''

#1.a#

ttl_shirts = 100

ttl_yellow = ttl_shirts // 2

ttl_green = ttl_shirts // 2

cost_t = 20

cost_green = cost_t * .75

cost_yellow = cost_t

ttl_green_cost = ttl_green * cost_green

ttl_yellow_cost = ttl_yellow * cost_yellow

ttl_cost = ttl_yellow_cost + ttl_green_cost

print(ttl_green, 'green t-shirts were purchased.')

print(ttl_yellow, 'yellow t-shirts were purchased.')

print('The total cost is ', ttl_cost)

print()

#1.b#

ttl_shirts = 101

ttl_yellow = ttl_shirts // 2

ttl_green = ((ttl_shirts - ttl_yellow))

cost_t = 20

cost_yellow = cost_t

cost_green = cost_t * .75

ttl_green_cost = ttl_green * cost_green

ttl_yellow_cost = ttl_yellow * cost_yellow

ttl_cost = ttl_yellow_cost + ttl_green_cost

print(ttl_green, 'green t-shirts were purchased.')

print(ttl_yellow, 'yellow t-shirts were purchased.')

print('The total cost is ', ttl_cost)

#expected result would be 1 more green then yellow for a total cost of 1765.0,#

#actual result is still 50/50 for 1750.0.#

print ()

#2.a#

g_orange = 7

g_green = g_orange * 3

g_purple = g_green + g_orange

g_red = g_purple * .5

g_yellow = 100 - (g_orange + g_purple + g_red + g_green)

total_g = (g_orange +  g_purple + g_red + g_green + g_yellow)

print(g_orange, 'total orange gummies')

print(g_green, 'total green gummies')

print(g_purple, 'total purple gummmies')

print(g_red, 'total red gummies')

print(g_yellow, 'total yellow gummies')

print(total_g, 'total gummies')


print()

#2.b#

g_orange = 8 #changed from 7 to 8#

g_green = g_orange * 3

g_purple = g_green + g_orange

g_red = g_purple * .5

g_yellow = 100 - (g_orange + g_purple + g_red + g_green)

total_g = (g_orange +  g_purple + g_red + g_green + g_yellow)

print(g_orange, 'total orange gummies')

print(g_green, 'total green gummies')

print(g_purple, 'total purple gummmies')

print(g_red, 'total red gummies')

print(g_yellow, 'total yellow gummies')

print(total_g, 'total gummies')

print()

#3.#

minutes_hour = 60

minutes_day = minutes_hour * 24

minutes_year = minutes_day * 365

print(minutes_year, 'minutes in a year')

#end#

