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

# this snippet takes inputs for 10 grades and outputs the average without using the average method

count = 0

for i in range(10):
    print("Grade #", i + 1, ":")
    grade = int(input(i))
    gradeTotal = gradeTotal + grade
    count += 1   

print("The average for the 10 grades is:", gradeTotal/count)

# %%
# throw exception for not integers
count = 0
grade = []
gradeTotal = 0

try:
    for i in range(10):
        print("Grade #", i + 1, ":")
        grade = int(input(i))
        gradeTotal = gradeTotal + grade
        count += 1

except ValueError:
    print("Only enter integers between 0 and 100.  Please try again.")

# %%
print("Grade #", i, ":")
grade = float(input(i))
print(grade, i)
# %%

# throw exception for non-integer values
count = 0
grade = []
gradeTotal = 0
choice = "y"

while choice.lower() == "y":
    try:
        for i in range(10):
            print("Grade #", i + 1, ":")
            grade = int(input(i))
            gradeTotal = gradeTotal + grade
            count += 1

    except ValueError:
        print("Only enter integers between 0 and 100.  Please try again.")
        choice = input("Would you like to try again? (y/n) ")

# %%
