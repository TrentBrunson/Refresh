# GIVEN: donut cost $1 for <6; >=6 costs $0.75

# input
numberDonuts = int(input("Today's prices are $1 per donut, and if you order 6 or more, they're 75 cents each!\n"
    "How many donuts would you like? "))

# print(type(numberDonuts)) - checking variable type

if numberDonuts < 6:
    donutCost = numberDonuts
else: 
    donutCost = numberDonuts * 0.75

print("Please pay $" + str(donutCost))

