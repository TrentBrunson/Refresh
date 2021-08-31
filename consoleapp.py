#!/usr/bin/env python3

import locale

# set locale to format currency
locale.setlocale(locale.LC_ALL, 'en_US')

# welcom msg
print("Welcome to the Future Value Calculator\n")

choice = 'y'

while choice.lower() == 'y':
    # user input
    monthly_investment = float(input("Enter your monthly investment:\t"))
    apr = float(input("Enter your annual percentage rate:\t"))
    years = int(input("Enter the number of years you will hold this investment:\t"))

    # convert interest rate to decimal format and years to compounding months
    monthly_interest_rate = apr/1200
    months = years * 12

    # calculate future value
    future_value = 0 # reset to 0 for each run
    for i in range(months):
        future_value = future_value + monthly_investment
        monthly_interest_amount = monthly_interest_rate * future_value
        future_value = future_value + monthly_interest_amount

    # display results
    print("Future value: \t\t" + locale.currency(future_value, grouping=True) + "\n")

    # ask to exit routine
    choice = input("Continue? (y/n): " + "\n")

# closing output
print("\nThank you for using the Future Value Calculator\n")
