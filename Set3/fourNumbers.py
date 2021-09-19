'''
2.	Special Number - Write a program that can find a four-digit number that has the four digits reversed when multiplied by four. 
For example, rstu * 4 = utsr. The program should report the number to the user. 
1.	No input
2.	List of digits *4 – [list of digits].reverse()
'''
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Find a Special 4-digit Number
# PURPOSE:    Find a 4-digit number that when the digits are reversed, it's the
#             original number times 4.
# INPUT:      No user input.
# PROCESS:    Create two numbers to begin the process.
#             Convert the numbers to strings to compare digits. 
#             Access each index of the strings to compare.
#             When all conditions are met, exit the subroutine.
# OUTPUT:     number of e's in the input
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
number = 1000 # start with the first 4 digit number in increment
solution = False

while solution == False:
    numX4 = number * 4
    # convert numbers to strings for comparison
    numStr1 = []
    numStr2 = []

    for i in str(number):
        numStr1.append(i)
    for i in str(numX4):
        numStr2.append(i)

    if numStr1[0] == numStr2[3] and numStr1[1] == numStr2[2] and numStr1[2] ==numStr2[1] and numStr1[3] == numStr2[0]:
        print(
            f"{numX4}'s digits are exactly four times and a palindrome of {number}."
        )
        solution = True
        continue
    else:
        solution = False
        number += 1
# %%
