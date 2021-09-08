#%%
# find words that have their letters arranged alphabetically
# supposedly less than 1k words like this in English

# ask user to input word

# edge case to think about
    # short words - is 1 letter sufficient?
    # duplicate letters

#%%
# # attempt with loop
choice = "Y"

while choice.upper() == "Y":
    print("This program will determine if you have an abecedarian word.")
    try:
        i = 0
        userWord = input("Enter you word:\n")
        for i in range(len(userWord) - 1):
            if userWord[i] > userWord[i + 1]:
                alpha = False
                break
            else: alpha = True
            # print(alpha) - logic check; need breakline to exit when false
        if alpha == False:
            print(f"Your word '{userWord}' does not have its letters in alphabetical order.")
        else:
            print(f"Your word '{userWord}' has all of its letters in alphabetical order!")
    except ValueError:
        print("Input words with letters only.\n")

    choice = input("Would you like to try again? (Y/N) ")
# %%
# logic error in for loops - switching approach
# working out logic for letter comparison
# sample snippet to test:
userWord = input("Enter you word:\n")
    # compare input to new sorted work
if list(userWord) == sorted(userWord):
    a = 'OK'
else:
    a = 'not OK'

print(a)
# %%
# this code finds words that have their letters arranged alphabetically
# attempt with boolean comparision
choice = "Y"

while choice.upper() == "Y":
    print("This program will determine if you have an abecedarian word.")
    try:
        userWord = input("Enter you word:\n")
    # compare input to new sorted work
        if list(userWord.lower()) == sorted(userWord.lower()):
            print(f"Your word '{userWord}' has all of its letters in alphabetical order!")
        else:
            print(f"Your word '{userWord}' does not have its letters in alphabetical order.")
    except ValueError:
        print("Input words with letters only.\n")

    choice = input("Would you like to try again? (Y/N) ") 
# %%
