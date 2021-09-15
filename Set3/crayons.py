'''5.	Crayon Colors - The file "Colors.txt   Download Colors.txt" 
contains the names of 123 crayon colors with one color per line. 
Write a program that asks the user to enter a letter of the alphabet 
and then displays all the colors that start with that letter. 
Write three separate functions: one to get the user input, 
one to build a list with the colors that start with the letter, 
and one to display the output. 
1.	Input function
    1.	Check only one character
2.	Find function
    1.	Cycle through list
    2.	Look at first value only and if true, append to new list
3.	Output function
    1.	Print list
'''
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Crayon Colors
# PURPOSE:    Find all of the colors that start with a user's letter of choice.
# INPUT:      A single letter
# PROCESS:    Compare input to colors.txt and see if the colors start with 
#             the letter given.
# OUTPUT:     Print list of colors that start with the user's letter.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
def getLetter():
    letter = str(input("Enter a letter of the alphabet:")).upper()
    return letter

def getColors(ltr):
    with open("data/Colors.txt") as file:
        word = ""
        newList, colorList = [], []
        for line in file:
            line = line.replace("\n", "")
            colorList.append(line)
        for word in colorList:
            if word.startswith(ltr):
                newList.append(word)
    return newList

def displayAnswer(letter, newList):
    print(f"Here are the colors that start with '{letter}':")
    for x in range(len(newList)):
        print(f'{newList[x]}')

def main():
    letter = getLetter()
    newList = getColors(letter)
    displayAnswer(letter, newList)

if __name__ == "__main__":
    main()
# %%
