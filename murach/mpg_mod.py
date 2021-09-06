#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()


choice = "y"

while choice.lower() == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_gallon = float(input("Enter cost per gallon:      "))
    print()

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)
        cost = gallons_used * cost_gallon
        print("Total Gas Cost:            ", round(cost, 2))
        cost_mile = cost / miles_driven
        print("Cost Per Mile:             ", round(cost_mile, 3), "\n")
    
    choice = input("Get entries for another trp (y/n)? ")
    print()

print("Bye!")
print()


