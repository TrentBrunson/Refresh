# US Federal Law requires that hourly employees be paid “time-and-a-half” for work in excess of 40 hours in one week. 
# User inputs hours worked in a week and the wage per hour. Displays gross pay. 

print(
    f"***********************************************************************\n"
    f"This program calculates weekly based on user inputs for wage and hours.\n"
    f"***********************************************************************\n\n"
)

wage = float(input("What is your hourly rate? "))
print()
weeklyHours = float(input("How many hours did you work? "))
print()

if weeklyHours < 40:
    grossPay = weeklyHours * wage
else:
    grossPay = (weeklyHours - 40) * wage * 1.5 + (wage * 40)

print(f"Your gross pay for the week is ${grossPay:.2f}\n")