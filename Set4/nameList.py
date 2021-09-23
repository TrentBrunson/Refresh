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
        
inputName = input("Enter first name:").capitalize()

if inputName in nameList:
    print(f"{inputName} already exists.")
else:
    with open("data/NewNames.txt", "w") as newF:
        nameList.append(f"{inputName}")
        nameList.sort()
        # use generator expression for large file sizes; writes piece-wise (https://www.delftstack.com/howto/python/python-writelines/)
        newF.writelines("%s\n" % item for item in nameList) 
    print(
        f"Your name {inputName}, did not appear in the list.\n"
        f"Your name {inputName}, has been added to the NewNames.txt file."
        )
# %%
# nameList, nameListUpper = [], []
def get_data_to_list():
    nameList = []
    print(
        f"This program will tell you if your entered name already exists in the list.\n"
        f"If not, it will add it to a list."
    )
    with open("data/names.txt") as file:
        for line in file:
            line = line.strip()
            nameList.append(line)
        print(*nameList)
    return nameList

def user_input():
    name = input("Enter first name:").capitalize()
    return name

def update_list_screen(inputName, nameList):
    print("\n\n", *nameList)
    if inputName in nameList:
        print(f"{inputName} already exists.")
    else:
        with open("data/NewNames.txt", "w") as newF:
            # nameList.append(f"{inputName}")
            nameList.append(f"{inputName}")
            nameList.sort()
            # use generator expression for large file sizes; writes piece-wise (https://www.delftstack.com/howto/python/python-writelines/)
            newF.writelines("%s\n" % item for item in nameList) 
        print(
            f"Your name {inputName}, did not appear in the list.\n"
            f"Your name {inputName}, has been added to the NewNames.txt file."
            )

def main():
    names = get_data_to_list()
    searchName = user_input()
    update_list_screen(searchName, names)

if __name__ == "__main__":
    main()
# %%
