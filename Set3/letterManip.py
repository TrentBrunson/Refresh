'''
1.	String Manipulation - Write a program that asks the user to enter a word or phrase and then displays the word or phrase with all occurrences of the letter "r" removed. Example: "Park the car in Harvard Yard" becomes "Pak the ca in Havad Yad."
    1.	Input sentence/phrase/word as list
    2.	Keep case
'''
#%%
str=input("What string would you like me to reformat? ")
removeLtr=['R','r'] 
filtered=filter(lambda i: i not in removeLtr,str) #lamda function
output="" 
for i in filtered: 
    output += i 
print(f"Here's your input with all of the letters 'r' removed:\n{output}")
# %%
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Letter r remover
# PURPOSE:    Remove the letters r in a string.
# INPUT:      user string of characters
# PROCESS:    create input and output functions and call with main
# OUTPUT:     User string displayed on screen without the letters r.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
def userInput():
    str=input("What string would you like me to reformat? ")

def screenOutput():
    print(f"Here's your input with all of the letters 'r' removed:\n{str.replace('R','').replace('r','')}")

def main():
    userInput()
    screenOutput()

if __name__ == "__main__":
    main()
# %%
str=input("What string would you like me to reformat? ")
print(f"Here's your input with all of the letters 'r' removed:\n{str.replace('R','').replace('r','')}")
# %%
