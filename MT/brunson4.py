# Trent Brunson
# Question 4

#%%
def makeJusticeTable():
    justiceTable = []
    file = "justices.txt"
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            currentLine = line.split(',')
            prez = currentLine[2]
            prezSurname = prez.split()
            lastName = [prezSurname[-1]]
            startYr = int(currentLine[4])
            if currentLine[5] == 0:
                endYr = startYr
                yearsServed = 0
            else:
                endYr = int(currentLine[5])
            yearsServed = endYr - startYr
            currentLine = currentLine + list(str(yearsServed)) + lastName
            justiceTable.append(currentLine)
            print(justiceTable)
    return justiceTable

def getInput():
    stateAbbrev = input("Enter a two-letter state abbreviation: ").upper()
    return stateAbbrev

def sortAndFilter(table, state2ltr):
    newtable = []
    for l in table:
        for item in l:
            if state2ltr in item:
                temp = l[0] + " " + l[1]
                lineTemp = [temp, l[-1], l[6]]
                # sortedList = lineTemp.sort()
                newtable.append(lineTemp)
    return newtable

def displayOutput(jt):
    print(
        f"Justice\t\tAppointed By\tYrs Served\n"
        f"******************************************"
    )
    # print(jt)
    # iterate through list of lists; line by line and print each item in line
    for line in jt:
        print(f"{line[0]}\t{line[1]}\t\t{line[2]}")
    return

def main():
    table = makeJusticeTable()
    state = getInput()
    filteredJustices = sortAndFilter(table, state)
    displayOutput(filteredJustices)

if __name__ == "__main__":
    main()
# %%
justiceTable = []
file = "justices.txt"
with open(file) as f:
    for line in f:
        line = line.rstrip()
        currentLine = line.split(',')
        prez = currentLine[2]
        prezSurname = prez.split()
        lastName = [prezSurname[-1]]
        startYr = int(currentLine[4])
        if currentLine[5] == 0:
            endYr = int(startYr)
        else:
            endYr = int(currentLine[5])
        yearsServed = int(endYr - startYr)
        currentLine = currentLine + list(str(yearsServed)) + lastName
        justiceTable.append(currentLine)
# print(justiceTable)

state = "KY"
for l in justiceTable:
    for item in l:
        if state in item:
            temp = l[0] + " " + l[1]
            lineTemp = [temp, l[-1], l[6]]
            # sortedList = lineTemp.sort()
            print(l, item, lineTemp)
            print("test")
# %%
