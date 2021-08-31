#%%
# BOGO for only 2 pairs of shoes

pair1 = float(input("Enter the price of the first pair of shoes: "))
pair2 = float(input("Enter the price of the second pair of shoes: "))

# compare shoe prices

if pair1 > pair2:
    total = pair1 + .5 * pair2
else:
    total = pair2 + .5 * pair1

print(f"Your total is ${total:.2f}")

#%%
# Bonus, do for infinite number of shoes

# inputs
    # create list for purchases
    # do you have another purchase
    # sort then count; if modulo - then take highest in list