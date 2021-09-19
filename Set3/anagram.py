#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Anagram Checker
# PURPOSE:    Compare two words or phrases to see if they're anagrams.
# INPUT:      User string 1 & 2.
# PROCESS:    Sort each string and compare if equal.
# OUTPUT:     Display if anagram is True or False
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
print("This program compares two words or phrases to see if they're anagrams.")
s1 = str(input("What is your first word or phrase? "))
s2 = str(input("What is your second word or phrase? "))

if sorted(list(s1.lower())) == sorted(list(s2.lower())):
    print(
        f"Your input '{s1}' IS an anagram of '{s2}.'\n"
    )
else: 
    print(
        f"Your input '{s1}' is NOT an anagram of '{s2}.'\n"
    )

# %%
def get_strings():
    s1 = str(input("What is your first word or phrase? "))
    s2 = str(input("What is your second word or phrase? "))
    return s1, s2

def string_sorter(sort1, sort2):
    compare = sorted(list(sort1.lower())) == sorted(list(sort2.lower()))
    return compare

def output(out1, out2):
    a = string_sorter(out1, out2)
    if a == True:
        print(
            f"Your input '{out1}' IS an anagram of '{out2}.'\n"
        )
    else: 
        print(
            f"Your input '{out1}' is NOT an anagram of '{out2}.'\n"
        )

def main():
    choice = "Y"
    while choice.upper() == "Y":
        user1, user2 = get_strings()
        output(user1, user2)
        choice = input("Continue? (Y/N) ")

if __name__ == "__main__":
    main()
# %%