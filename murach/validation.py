# this provides validation modules for other programs

def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)

def main():
        choice = "Y"
        while choice.upper() == "Y":
            valid_number = get_float("Enter number: ", 0, 1000)
            print("Valid number = ", valid_number, "\n")
            valid_integer = get_int("Enter integer: ", 0, 50)
            print("Valid integer = ", valid_integer, "\n")

            # user continue?
            choice = input("Continue? (Y/N) ")
        print("¡Adios!")

if __name__ == "__main__":
    main()