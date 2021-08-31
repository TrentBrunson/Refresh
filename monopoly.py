# Tell the user which property is not a RR
print("Here are the 4 Monopoly railroad properties.  Which one is not a true railroad?\n" + 
    "1. B&O\n"
    "2. Pennsylvania\n"
    "3. Reading\n"
    "4. Short Line"
    )

choice = "y"

while choice.lower() == "y":

    guess = input("Which railroad do you think is not a real railroad? Enter the number of your choice: ")

    if int(guess) == 4:
        print("That is correct!")
        choice = "n"
    else:
        print("Sorry, that is wrong.")
        choice = input("Would you like to try again? (y/n): ")

print("Hope you had fun playing with Monopoly railroads.  Come back soon!")