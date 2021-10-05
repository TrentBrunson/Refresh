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
            lastName = prezSurname[-1]
            if currentLine[5] == '0':
                endYr = 2020
            else:
                endYr = int(currentLine[5])
            startYr = int(currentLine[4])
            yearsServed = endYr - startYr
            currentLine.extend((yearsServed, lastName))
            justiceTable.append(currentLine)
    return justiceTable

def getInput():
    stateAbbrev = input("Enter a two-letter state abbreviation: ").upper()
    return stateAbbrev

def sortAndFilter(table, state2ltr):
    newtable = []
    for l in table:
        if state2ltr in l:
            temp = l[0] + " " + l[1]
            lineTemp = [temp, l[-1], l[6]]
            newtable.append(lineTemp)
    sortedList = sorted(newtable, key = lambda x: int(x[-1]), reverse=True)
    return sortedList

def displayOutput(jt):
    print(
        f"{'Justice':25}{'Appointed By':15}{'Yrs Served':10}\n"
        f"**************************************************"
    )
    for line in jt:
        print(f"{line[0]:25}{line[1]:<10}{line[2]:>10}")
    return

def main():
    table = makeJusticeTable()
    state = getInput()
    filteredJustices = sortAndFilter(table, state)
    displayOutput(filteredJustices)

if __name__ == "__main__":
    main()
# %%
