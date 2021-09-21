#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    First Name Collection
# PURPOSE:    Extract values from file and display to user on screen.
# INPUT:      File with name data and user selection.
# PROCESS:    Import data file.  Get user input.  If extant, report back to user.
#             If not found, add to file and report insertion completed.  
#             Write to new file.  Handle exceptions.
# OUTPUT:     Report to user on screen and create new file with new names.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
# %%
nameList, nameListUpper = [], []

print(
    f"This program will tell you if your entered name already exists in the list.\n"
    f"If not, it will add it to a list."
)
with open("data/names.txt") as file:
    for line in file:
        line = line.strip()
        nameList.append(line)
        
name = input("Enter first name:").capitalize()

if name in nameList:
    print(f"{name} already exists.")
else:
    with open("data/NewNames.txt", "w") as newF:
        nameList.append(f"{name}")
        nameList.sort()
        # use generator expression for large file sizes; writes piece-wise (https://www.delftstack.com/howto/python/python-writelines/)
        newF.writelines("%s\n" % item for item in nameList) 
        # newF.writelines("%s\n" % item for item in nameList) 
    print(
        f"Your name {name}, did not appear in the list.\n"
        f"Your name {name}, has been added to the NewNames.txt file."
        )
# %%
