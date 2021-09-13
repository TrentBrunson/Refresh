def calculate_future_value(monthly_investment, yearly_interest, years): # convert yearly values to monthly values monthly_interest_rate = yearly_interest / 12 / 100 months = years * 12
    # calculate future value 
    future_value = 0.0 
    for i in range(1, months):
        future_value += monthly_investment_amount 
        monthly_interest = future_value * monthly_interest_rate 
        future_value += monthly_interest
    return future_value

#%%

#print(f"You entered {guess}")  
again = "Y"
while again.lower() == "y":
    guess = input("Enter your guess: ")
    if guess.lower() == "c":
        print("Yes, correct!")
        break
    elif guess.lower() == "a" or "b" or "d":
        print("Sorry, incorrect.")
        again = input("Guess again? (y/n) ")
print("Bye!")
# %%
