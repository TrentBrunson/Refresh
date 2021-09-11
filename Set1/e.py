#%%
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Letter e counter
# PURPOSE:    Count the letter e in a string.
# INPUT:      user string of characters
# PROCESS:    treat the input string as a list of characters
# OUTPUT:     number of e's in the input
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# loop method

print("Welcome to the Sesame Street letter counter!!!\nToday we are counting the letter E!\n\n")

ssinput = input("What word(s) would you like me to count for you?\n")

count = 0 #reset counter to 0

for i in ssinput.lower():
    if i == 'e':
        count += 1

print ("The Count of \"E\" in '" + ssinput + "' is: " + str(count))

# %%
# alternate method to get string counts

print("Welcome to the Sesame Street letter counter!!!\nToday we are counting the letter E!\n\n")

ssinput = input("What word(s) would you like me to count for you?\n").lower()
count = ssinput.count('e')

print ("The Count of \"E\" in '" + ssinput + "' is: " + str(count))

# %%
# this time ask for user input on what letter to count

print("Welcome to the Sesame Street letter counter!!!\n")

ssString= input("What word(s) would you like me to count for you?\n")
ssChar = input("What letter would you like me to count for you?\n")

ssStringLower = ssString.lower()
ssCharLower = ssChar.lower()
count = 0

for i in ssStringLower:
    if i == ssCharLower:
        count += 1

print("The count of '" + ssChar + "' in '" + ssString + "' is: " + str(count))

# %%
