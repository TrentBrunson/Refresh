#%%
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Leap Year
# PURPOSE:    Determine if a given year is a leap year.
# INPUT:      User year.
# PROCESS:    Step through the logic of leap year determination with if statements.
# OUTPUT:     A statement saying whether the input is a leap year or not.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# code snippet to take user input and return if a leap year or not

# leap years have no remainder if divided by 4
    # except if divisible by 100
        # except if divisible by 400
        # invert this order
year = int(input("Which year do you want if it is a leap year or not?"))

if year % 400 == 0: 
    print("Yes,", year, "is a leap year.")
elif year % 100 == 0:
    print("No,",year, "is NOT a leap year.")
elif year % 4 == 0:
    print("Yes,", year, "is a leap year.")
else:
    print("No,", year, "is NOT a leap year." )

#%%
# edge cases
    # what about years BC?

# %%
year = int(input("Which year do you want if it is a leap year or not?"))

if year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0): 
    print("Yes,", year , "is a leap year.")
else:
    print("No,", year , "is NOT a leap year.")

# %%
