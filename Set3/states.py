'''
The data file "States.txt" contains the 50 US states 
in order they joined the union with one state per line. 
Write a program to read the file contents into a list. 
Then sort the list based on the number of consonants 
contained in the state name in ascending order. 
HINT: You will need to write a function to count 
the number of consonants in a word. 
'''
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
#%%
def welcome():
    print(f"This program reorders a list of states by the number of\n"
        f"consonants in the name and displays them in ascending order.\n"
    )

# ID which letters are consonants in string of characters
def consonants (char):
    char = str(char).lower()
    return not(
        char == 'a' or char == 'e' or char == 'i' or
        char == 'o' or char == 'u' or char == " "
    )

# count consonants in word
def countConsonants(stateName):
    count = 0 # reset counter each time f(x) is called
    for i in range(len(stateName)):
        if (consonants(stateName[i])): # call consonant f(x)
            count += 1
    return count

# transform text file to a list of strings
def getStates():
    state = ""
    statesSorted = []
    l = []
    stateList = []
    with open("data/States.txt") as file:        
        for line in file:
            line = line.replace("\n", "")
            stateList.append(line)
        for state in stateList:
            length = countConsonants(state)
            l.append(length)
            # newlist.append(group)
        temp = list(zip(l, stateList))
        temp.sort()
        statesSorted = [item[1] for item in temp]
    return statesSorted

def output(statesSorted):
    print(f"Here is the new list of states ordered by number of consonants:")
    print(*statesSorted, sep = "\n")

def main():
    welcome()
    statesSorted = getStates()
    output(statesSorted)

if __name__ == "__main__":
    main()
# %%
