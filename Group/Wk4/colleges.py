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
        f"colleges founded before 1800 in that state, sorted by founding year.\n"
    )

def user_input():
    twoLtrState = input("Enter the two-letter abbreviation for the state: ").upper()
    print(twoLtrState)
    return twoLtrState

def find_colleges(state, collegeList):
    outputList = []
    found = False
    for i in range(len(collegeList)):
        collegeList[i] = collegeList[i].split(",")
        collegeList[i][2] = int(collegeList[i][2]) # change year to int for sorting
    collegeList.sort(key=lambda college: college[2]) #sort by year
    
    for college in collegeList:
        if college[1] == state:
            outputList.append([collegeList[0], collegeList[2]])
            print(*collegeList[0], *collegeList[2])
            found = True
    outputList.sort()
    print(outputList)
    if not found:
        print(f"There are no early colleges from {state}.")
    return outputList

def display_results(printList):
    print(printList)

def main():
    display_header()
    stateCollege = read_file_to_list()
    choice = user_input()
    screenList = find_colleges(choice, stateCollege)
    print(screenList)
    display_results(screenList)

if __name__ == "__main__":
    main()