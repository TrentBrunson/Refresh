# User inputs 2-letter state abbreviation and program returns
# colleges in that state with years founded, sorted by founding year.

def read_file_to_list():
    filePath = "Group\Wk4\Colleges.txt"
    # filePath2 = "Colleges.txt"
    with open(filePath, "r") as infile:
        states = [line.rstrip() for line in infile]
        return states

def display_header():
    # tell user what the program does
    print(
        f"User inputs 2-letter state abbreviation and program returns\n"
        f"colleges in that state with years founded, sorted by founding year.\n"
    )

def user_input():
    twoLtrState = input("Enter the two-letter abbreviation for the state: ")
    return twoLtrState

def find_colleges(state, collegeList):
    outputList = []
    for state in collegeList:
        outputList.append(state)
    return outputList

def display_results():
    return

def main():
    display_header()
    stateCollege = read_file_to_list()
    choice = user_input()
    find_colleges(choice, stateCollege)
    display_results()

if __name__ == "__main__":
    main()