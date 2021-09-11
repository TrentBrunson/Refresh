#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    
# PURPOSE:     
# INPUT:      
# PROCESS:    
# OUTPUT:     
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# Aa program to make change for an amount of money from 0 through 99 cents input by the user. 
# Show the number of coins from each denomination (i.e., quarters, dimes, nickels, and pennies) used to make the change. 

print(
    f"****************************************\n"
    f"This program calculates how make change.\n"
    f"****************************************\n"
)

change = int(input("Enter how much change you need to make in coins (0-99): "))
print()

quarters = change // 25
dimes = (change - (quarters * 25)) // 10
nickels = (change - (quarters * 25) - (dimes * 10)) // 5
pennies = change - (quarters * 25) - (dimes * 10) - (nickels * 5)

print(
    f"To make your change you need:\n"
    f"Quarters: {quarters}\n"
    f"Dimes:    {dimes}\n"
    f"Nickles:  {nickels}\n"
    f"Pennies:  {pennies}\n"
)
 