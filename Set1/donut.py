#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Donut Shop Till
# PURPOSE:    Figure out the total cost for the donut order.
# INPUT:      Number of donuts.
# PROCESS:    Determine which threshold the donuts fall into and charge the correct total price.
# OUTPUT:     Total price.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# GIVEN: donut cost $1 for <6; >=6 costs $0.75

# input
numberDonuts = int(input("Today's prices are $1 per donut, and if you order 6 or more, they're 75 cents each!\n"
    "How many donuts would you like? "))

# print(type(numberDonuts)) - checking variable type

if numberDonuts < 6:
    donutCost = numberDonuts
else: 
    donutCost = numberDonuts * 0.75

print("Please pay $" + str(donutCost))

