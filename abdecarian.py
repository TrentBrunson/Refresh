#%%
# find words that have their letters arranged alphabetically
# supposedly less than 1k

# ask user to input word

# edge case to think about
    # short words - is 1 letter sufficient?
    # duplicate letters

#%%
choice = "Y"

while choice.upper() == "Y":
    print("This program will determine if you have an abdecarian word.")
    try:
        userWord = input("Enter you word:")
        for i in range(len(userWord) - 1):
            if userWord[i] > userWord[i + 1]:
                alpha = False
            else: alpha = True
            if alpha == False:
                print("Your {userWord} does not have its letters in alphabetical order.")
            else:
                print("Your {userWord} has all of its letters in alphabetical order!")
    except ValueError:
        print("Input words with letters only.\n")

    choice = input("Would you like to try again? (Y/N) ") 