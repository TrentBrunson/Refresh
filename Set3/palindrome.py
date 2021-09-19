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
# Replace special characters with '' and reverse second string for compare
s1Stripped = list(''.join(ch for ch in s1 if ch.isalnum()).lower())
s2RevStripped = list(reversed(''.join(ch for ch in s2 if ch.isalnum()).lower()))

if s1Stripped == s2RevStripped:
    print(
        f"Your words {s1} and {s2} are a palindrome."
    )
else: print(f"You do not have a palindrome.")
print(s2RevStripped)
# %%
def str_rev(string):
    return string[::-1]

def get_words():
    s1 = str(input("Enter your first word or phrase: "))
    s2 = str(input("Enter your second word or phrase: "))
    return s1, s2

def alpha_num_word(a1, a2):
    # get only alphanumerics and convert to lower case for comparison
    # reverse second string for comparison
    s1Stripped = list(''.join(ch for ch in a1 if ch.isalnum()).lower())
    s2Stripped = list(''.join(ch for ch in a2 if ch.isalnum()).lower())
    s2Rev = str_rev(s2Stripped)
    return s1Stripped, s2Rev

def palindrome(p1, p2, s1, s2):
    if p1 == p2:
        print(
            f"Your words {s1} and {s2} are a palindrome."
        )
    else: print(f"You do not have a palindrome.")
    return 

def main():
    choice = "Y"
    print("This program determines if your inputs are plaindromes.")
    while choice.upper() == "Y":
        user1, user2 = get_words()
        noSpecial1, noSpecial2 = alpha_num_word(user1, user2)
        palindrome(noSpecial1, noSpecial2, user1, user2)
        choice = input("Would you like to try another set or phrase? (Y/N)")

if __name__ == "__main__":
    main()
# %%