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
#%%
choice = "Y"
while choice.upper() == "Y":
    # units = "septillion,sextillion,septillion,quadrillion,trillion,billion,million,thousand,".split(',')
    units = " ,thousand,million,billion,trillion,quadrillion,quintillion,sextillion,septillion,".split(',')
    number = int(input("Enter your number: "))
    numberStr = str(number)
    length = len(numberStr)
    thou = 1000
    n = 0
    i=1
    if length > 27:
        print("What are you thinking?  Input a number less than an octillion!!")
        break
    if number <= 0:
        print("Enter a number greater than zero")
    elif length <=3:
        print(f"Your number is: {number}")
        break
    
    while length > 0:
        x = number // 10 ** (i * 3)
        print(f"{x}\t{units[round(length/3)-1]}\n")
        i += 1
        n+=1
        length -=3
    choice = input("Would you like to enter another number? (Y/N)")

#%%
    # loopLength = length / 3

    # while length > 0:
    #     out = number // 10000
    #     out.append()
    #     length -= 3
        
    # wordOut, numOut = [], []
    # nList = []

    # out = number // (thou * 7)

    # if (number // thou ** 9) != 0:
    #     print(f"{(number // thou ** 9)}\tseptillion\n")
    #     nList = numberStr[3:]
    #     print(nList)
    # if (nList // thou ** 8) != 0:
    #     print(f"{(number // thou ** 8)}\tsextillion\n")
    # if (number // thou ** 7) != 0:
    #     print(f"{(number // thou ** 7)}\tquintillion\n")
    # if (number // thou ** 6) != 0:
    #     print(f"{(number // thou ** 6)}\tquadrillion\n")
    # if (number // thou ** 5) != 0:
    #     print(f"{(number // thou ** 5)}\ttrillion\n")
    # if (number // thou ** 4) != 0:
    #     print(f"{(number // thou ** 4)}\tbillion\n")
    # if (number // thou ** 3) != 0:
    #     print(f"{(number // thou ** 3)}\tmillion\n")
    # if (number // thou ** 2) != 0:
    #     print(f"{(number // thou ** 2)}\tthousand\n")
    # if (number // thou) != 0:
    #     print(f"{(number // thou)}\t\n")


    # numberslicer = numberStr[-3:]
    # print(numberslicer)
    # numberslicer = [numberStr[i : i+3] for i in range(0, length, 3)]
    # backwards = []
    # step = -3
    # while i < length:
    #     temp = numberStr[::-1]
    #     backwards.append(temp)
    #     i += 3
    # print(numberslicer, backwards)
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
19%10
# %%
(12345678912//1000000000)
# %%
12 // 100
# %%
12 % 100
# %%
units = "septillion,sextillion,septillion,quadrillion,trillion,billion,million,thousand,".split(',')
print(units)
testy = units[5]
print(testy)
# %%
a = '1234567891012'
n = 3
out = [a[k:k+n] for k in range(-len(a),0, -3)]
print(out)
# %%
# initializing list
test_list = [4, 5, 2, 6, 7, 8, 10]
 
# printing original list
print("The original list : " + str(test_list))
 
# using list slicing
# Get last N elements from list
res = test_list[-3:]
 
# print result
print("The last N elements of list are : " + str(res))

trunc = test_list[:len(test_list)-3]
print(*trunc)
# %%
for i in range(length) > 0:
    x = number % 10 ** (i * 3)
    print(f"{x}\t{units[i]}\n")
    i -= 3
# %%
number = int(input("Enter your number: "))
x = number % 10 ** (1 * 3)
print(x)
# %%
123456 % 10 ** (2 * 3)

# %%
units = " ,thousand,million,billion,trillion,quadrillion,quintillion,sextillion,septillion,".split(',')
print(*units)
# %%

# %%
