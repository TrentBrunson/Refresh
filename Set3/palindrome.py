'''
3.	Check for Palindromes - prompts the user to enter a word or phrase. 
Then check to see if the word is a palindrome. 
A palindrome reads the same forward and backward ignoring punctuation and spaces. 
For example, "racecar," "Madam, I'm Adam," and "Anna." 
1.	Input
2.	Split in half
    1.	What if odd
        1.	splitpoint = for i in range (len(string) % 2)
        2.	else: - no need, line above works for both odd and even
        3. or count backwards form end of list
    2.	assign second string to a list
3.	reverse order for second half

'''
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Palindrome
# PURPOSE:    Identify if the two inputs meet the criteria of a palindrome.
# INPUT:      User input two strings of words or phrases.
# PROCESS:    Strip puntucation and spaces.  Reverse order of second input and compare.
# OUTPUT:     If true, display acknowledgement that inputs are a palindrome, otherwise, no.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
print("This program determines if your inputs are plaindromes.")

s1 = str(input("Enter your first word or phrase: "))
s2 = str(input("Enter your second word or phrase: "))
# Replace special characters with ''
s1Stripped = list(''.join(ch for ch in s1 if ch.isalnum()))
# s2Stripped = list(''.join(ch for ch in s2 if ch.isalnum()))
s2RevStripped = list(reversed(''.join(ch for ch in s2 if ch.isalnum())))

# s2RevStripped = list(reversed(s2Stripped))

if s1Stripped == s2RevStripped:
    print(
        f"Your words {s1} and {s2} are a palindrome."
    )
else: print(f"You do not have a palindrome.")
print(s2RevStripped)
# %%
