#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Reading Numbers
# PURPOSE:    Read an integer less than an octillion and display the units of the numbers.
# INPUT:      A positive integer less than an octillion.
# PROCESS:    Take the input, convert to string and to list.  Find the length of string.
#             Handle edge cases and exceptions.  Revers the new number list to prepare it for
#             for grouping by threes.  Once grouped by threes from smallest to largest units, 
#             reverse the the order of the sublists.  Iterate through the new list, slicing the 
#             information needed to print to screem.
# OUTPUT:     Two columns of information with numbers in the left hand column and the units in 
#             the right hand column, starting from highest to lowest units.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
# %%
"""
Pseudocode
Write a program that asks the user to enter a number with 27 digits or less. 
The convert that number into a set of three-digit numbers and associated 
place values. Display the results to the user.
"""
#%%
choice = "Y"
while choice.upper() == "Y":
    units = " ,thousand,million,billion,trillion,quadrillion,quintillion,sextillion,septillion,".split(',')
    number = int(input("Enter your number: "))
    numberList = list(str(number))
    length = len(numberList)
    i = 0

    print(f"Your number: {number}")
    if length > 27:
        print("What are you thinking?  Input a number less than an octillion!!")
        continue
    if number <= 0:
        print("Enter a number greater than zero.")
        continue
    elif length <=3:
        print(f"Your number is: {number}")
        continue        
    
    # List manipulation    
    numberList.reverse()  # reverse the string
    # group the string in groups of 3s in a list of lists
    subList = [numberList[n:n+3] for n in range(0, len(numberList), 3)]
    # reverse the order of the sublists
    subList = [n [::-1] for n in subList][::-1]

    while length > 0:
        print(f"{''.join(str(j) for j in subList[i])}\t{units[((length-1)//3)]}")
        i += 1
        length -=3
    choice = input("Would you like to enter another number? (Y/N)")
# %%
def list_manipulator(numList, size):
    # List manipulation    
    numList.reverse()  # reverse the string
    # group the string in groups of 3s in a list of lists using list comprehension
    subList = [numList[n:n+3] for n in range(0, size, 3)]
    # reverse the order of the sublists
    subList = [n [::-1] for n in subList][::-1]
    return subList

def to_screen(length, l, units):
    i = 0
    while length > 0:
        print(f"{''.join(str(j) for j in l[i])}\t{units[((length-1)//3)]}")
        i += 1
        length -=3
    return

def get_num():
    choice = "Y"
    while choice.upper() == "Y":
        units = " ,thousand,million,billion,trillion,quadrillion,quintillion,sextillion,septillion,".split(',')
        number = int(input(
            f"When you enter a positive integer, this program displays the units of the numbers."
            f"Enter your number: "))
        numberList = list(str(number))
        length = len(numberList)

        print(f"Your number: {number}")
        if length > 27:
            print("What are you doing?  Trying to crash the system?  Input a number less than an octillion!!")
            continue
        if number <= 0:
            print("Enter a number greater than zero.")
            continue
        elif length <=3:
            print(f"Your number is: {number}")
            continue
        formattedList = list_manipulator(numberList, length)
        to_screen(length, formattedList, units)
        choice = input("Would you like to enter another number? (Y/N)")
    return number, numberList, length, units

def main():
    get_num()
    return

if __name__ == "__main__":
    main()
# %%