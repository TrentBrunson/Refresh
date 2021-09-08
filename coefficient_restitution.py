"""
This program takes a user input for the coefficient of restitution (meaning to what percentage
will the object bounce back to the original height of the drop).  It uses this to output how 
bounces until the object's bounce is less than 10 inches.
"""

coRestitution = float(input("What is your coefficient of restitution? (0.0-.99) "))
print()
ftHeight = float(input("What is your starting height in feet? "))
print()
count = 1
height = ftHeight * 12
totalDistance = 0

while height > 10:
    height = height * coRestitution
    totalDistance = totalDistance + height
    print(
        f"Bounce #{count}\n"
        f"New height:       {height:.0f} inches\n"
        f"Total distance:   {totalDistance:.0f} inches\n"
    )
    count += 1

print(f"Your object bounced {count-1} times and traveled a total of {totalDistance / 12:.2f} feet.")