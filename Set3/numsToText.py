#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Reading Numbers
# PURPOSE:    Count the letter e in a string.
# INPUT:      user string of characters
# PROCESS:    treat the input string as a list of characters
# OUTPUT:     number of e's in the input
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
# %%
"""
Pseudocode
Write a program that asks the user to enter a number with 27 digits or less. 
The convert that number into a set of three-digit numbers and associated 
place values. Display the results to the user.
"""

choice = "Y"
while choice.upper() == "Y":
    number = int(input("Enter your number: "))
    numberStr = str(number)
    length = len(numberStr)
    print(length)

    if number <= 0:
        print("Enter a number greater than zero")
    else:
        for i in range (length//3):
            i = 3

    units = "septillion sextillion septillion quadrillion trillion billion million thousand".split()

    # numberslicer = numberStr[-3:]
    # print(numberslicer)
    numberslicer = [numberStr[i : i+3] for i in range(0, length, 3)]
    backwards = []
    step = -3
    while i < length:
        temp = numberStr[::-1]
        backwards.append(temp)
        i += 3
    print(numberslicer, backwards)

    choice = input("Would you like to enter another number? (Y/N)")



# %%
x = [1,2,3,4,5,6,7,8,9]
n=3
test = zip(*[iter(x)]*3)
test2 = map(None, *[iter(x)]*3)
print(test, test2)
# %%
l = range(9)
a = zip(*([l]*3))
print(a)
# %%
line = '1234567890'
n = 3
b = [line[i:i+n] for i in range(0, len(line), n)]
print(b)
# %%
number = int(input("Enter your number: "))
numberStr = str(number)
length = len(numberStr)
print(length)

if number <= 0:
    print("Enter a number greater than zero")

print(reverse)
backwards = []
while i < length:
    step = 0
    temp = reverse[step:3]
    backwards.append(temp)
    step += 3
    i += 3
print(numberslicer, backwards)
# %%
19%10
# %%
(12345678912//1000000000) % 100
# %%
12 // 100