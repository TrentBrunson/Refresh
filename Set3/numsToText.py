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
    numberList = list(str(number))
    length = len(numberList)
    print(length)
    thou = 1000
    n = 0
    i = 0

    print(f"Your number: {number}")
    if length > 27:
        print("What are you thinking?  Input a number less than an octillion!!")
        break
    if number <= 0:
        print("Enter a number greater than zero.")
    elif length <=3:
        print(f"Your number is: {number}")
        break
    
    # List manipulation    
    numberList.reverse()  # reverse the string
    # group the string in groups of 3s in a list of lists
    subList = [numberList[n:n+3] for n in range(0, len(numberList), 3)]
    # print(numberList,length, "\n", subList, "\n", len(subList), subList)
    # reverse the order of the sublists
    subList = [n [::-1] for n in subList][::-1]
    # print(subList)

    while length > 0:
        x = number // 10 ** (round(length/3) * 3)
        # print()
        # print(numberList,x)
        # print(f"{subList[i]}\t{units[round(length/3)]}\n")
        # print(''.join(str(j) for j in subList[i]))
        print(f"{''.join(str(j) for j in subList[i])}\t{units[((length-1)//3)]}\n")

        # numberStr = numberStr[length:]
        i += 1
        n += 3
        length -=3
        print(length, i, n)
    choice = input("Would you like to enter another number? (Y/N)")

#%%
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
n = 5
mylist = [1,2,3,4,5,6,7,8,9]
newlist = mylist[n:]
print (newlist)
# %%
n = 5
mylist = [1,2,3,4,5,6,7,8,9]
del mylist[:n]
print(mylist)
# %%
theList = list(range(10))
l = len(theList)
N = 3
print(*theList)
# len(theList)
# revL = theList.reverse()
subList = [theList[n:n+N] for n in range(0, len(theList), N)]
print(theList,l, "\n", subList, "\n", len(subList))
# %%
7//3
# %%
10//3
# %%
3//3
# %%
2//3
# %%
4//3
# %%
4%3
# %%
5%3
# %%
6%3
# %%
numberStr = [1,2,3,4,5,6,7]
length = len(numberStr)
revL = numberStr.reverse()
subList = [numberStr[n:n+3] for n in range(0, len(numberStr), 3)]
print(numberStr,length, "\n", subList, "\n", len(subList), subList)
subList = [elem [::-1] for elem in subList][::-1]
print(subList)
# %%
numberStr = [1,2,3,4,5,6,7]
# length = len(numberStr)
numberStr.reverse()
subList = [numberStr[n:n+3] for n in range(0, len(numberStr), 3)]
print(numberStr,length, "\n", subList, "\n", len(subList), subList)
subList = [n [::-1] for n in subList][::-1]
print(*subList[2])
print(''.join(str(i) for i in subList[2]))
# subList = []
# %%
num = 12345679
type(num)
num1 = list(str(num))
print(num1)
# %%
