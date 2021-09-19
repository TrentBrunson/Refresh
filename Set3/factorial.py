'''
4.	Calculate the Factorial - The factorial of a positive integer is the product 1 * 2 * 3 * 4 ... * n where n represents the positive integer. 
Write a program that asks the user to enter a positive integer and calculates the factorial. 
Use a main() function to control the program flow. 
Write a function to get an integer from the user and verify the user entered a positive integer value. 
Write a different function to calculate the factorial for a number. 
1.	Input function & check positive
2.	Calc function
1.	Create list of values
2.	Iterate through list, multiplying values

'''
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Factorial
# PURPOSE:    Compute the factorial of positive number.
# INPUT:      User number.
# PROCESS:    Iterative: input * (input-1) while input > 0.
# OUTPUT:     Factorial of user number
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
#%%
choice = "Y"

print("This program calculates the factorial of a number.")

while choice.upper() == "Y":
    num = int(input("Enter a positive whole number: "))
    answer = 1
    i = num

    while i > 1:
        answer *= (i)
        i -= 1
        print(i, num, answer)
    
    print(f"The factorial of {num} is: {answer}\n")
    choice = input("Would you you like to try again? (Y/N)")
#%%
def number():
    num = int(input("Enter a positive whole number: "))
    return num

def factorial(factorNum):
    i = factorNum
    while i > 1:
        factorNum *= (i - 1)
        i -= 1
    return factorNum

def output(numIn):
    answer = factorial(numIn)    
    print(f"The factorial of {numIn} is: {answer}\n")

def main():
    print("This program calculates the factorial of a number.")
    choice = "Y"
    while choice.upper() == "Y":
        userNumber = number()
        if userNumber < 0:
            print("Let's do factorials of positive numbers only please.  Thank you.")
            continue
        output(userNumber)
        choice = input("Would you you like to try again? (Y/N)")

if __name__ == "__main__":
    main()
# %%