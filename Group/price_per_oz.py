#%%
#!/usr/bin/env python3

# A program that requests the price and weight of an item in pounds and ounces, and then determines the price per ounce. 

print(
    f"************************************************************************\n"
    f"This takes the weight and price of product and displays price per ounce.\n"
    f"************************************************************************\n\n"
)

print("What is your item weight in pounds and ounces:\n")
# print("Pounds: ")
# print("Ounces: ")
print()

# typecast string input as integer using list comprehension
weightPound, weightOunce = [int(x) for x in input().split()]

price = float(input("Enter the price of your product: "))

ozPrice = price / (weightPound * 16 + weightOunce) 

print(f"Your item costs ${ozPrice:.2f} per ounce.")
# %%
# A program that requests the price and weight of an item in pounds and ounces, and then determines the price per ounce. 

print(
    f"************************************************************************\n"
    f"This takes the weight and price of product and displays price per ounce.\n"
    f"************************************************************************\n\n"
)

weightPound, weightOunce = input("What is your item weight in pounds and ounces:\n").split()
# print("Pounds: ")
# print("Ounces: ")
print()

price = float(input("Enter the price of your product: "))

ozPrice = (weightPound * 16 + weightOunce) * price

print(f"Your item costs ${ozPrice:.2f} per ounce.")
# %%

# Reads two numbers from input and typecasts them to int using 
# list comprehension
word, wd = [int(x) for x in input().split()] 

print(word * wd)
# %%
