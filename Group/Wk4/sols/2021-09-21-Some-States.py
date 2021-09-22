def displayHeader():
    # print the header
    print("Parse States")
    print()

def readFileToList():
    with open("SomeStates.txt", "r") as infile:
        states = [line.rstrip() for line in infile]
        return states

def splitStates(states):
    vowels = "aeiou"
    vowelStates = []
    consonantStates = []
    for state in states:
        if state[0].lower() in vowels:
            vowelStates.append(state)
        else:
            consonantStates.append(state)
    return vowelStates, consonantStates

def writeStates(vStates,cStates):
    with open("VowelStates.txt","w") as outfile:
        vStates.sort()
        for state in vStates:
            outfile.write(f"{state}\n")

    with open("ConsonantStates.txt","w") as outfile:
        cStates.sort()
        for state in cStates:
            outfile.write(state + "\n")

def main():
    displayHeader()
    statesList = readFileToList()
    #print(statesList)
    vStates, cStates = splitStates(statesList)
    #print(vStates,cStates)
    writeStates(vStates,cStates)


if __name__ == "__main__":
    main()
    
