# Trent Brunson
# Question 4
#%%
prez = {}
prezNum = 0
file = "USPres.txt"
counter = 1
start = int(input("Enter start #: "))
end = int(input("Enter end #: "))

with open(file) as f:
    for line in f:
        prezNum += 1
        line = line.strip()
        prez[prezNum] = line
# ************************************************      
        if counter >= start and counter <= end:            
            print (f"{counter}\t{line.strip()}")            
            counter += 1        
        else:            
            counter += 1

# print(type(prez))
# for num in prez.keys():
#     print(f"{num}")
# print(prez)
# %%
choice = "Y"
while choice == "Y":
    try:
        start = int(input("Which number of president do you wish to start with?"))
        end = int(input("Which number of president do you wish to end with?"))
    except ValueError:
        print("Only enter integers please.")
        continue
    if end < start:
        print("Your starting number must be less than your ending number.")
        continue
    elif end > 46:
        print("There are only 45 presidents in this database, enter a value less than 46 please.")
        continue
    elif start < 1:
        print("You must start with at least the first president; enter a value of 1 to 46.")
        continue

    print(start,end)
    # call displayOutputs()
    choice = input("Contimue? (Y/N) ").upper()

print(start,end)
# %%
def displayOutputs(start, end):
    prez = {}
    prezNum = 0
    file = "USPres.txt"

    with open(file) as f:
        for line in f:
            prezNum += 1
            line = line.strip()
            prez[prezNum] = line
    
    for i in range(start, end + 1):
        temp = prez[i]
        print(f"{i} {temp}")

    return

def getInputs():
    choice = "Y"
    while choice == "Y":
        try:
            start = int(input("Which number of president do you wish to start with?"))
            end = int(input("Which number of president do you wish to end with?"))
        except ValueError:
            print("Only enter integers please.")
            continue
        if end < start:
            print("Your starting number must be less than your ending number.")
            continue
        elif end > 46:
            print("There are only 46 US presidents in this database, enter a value less than 46 please.")
            continue
        elif start < 1:
            print("You must start with at least the first president; enter a value of 1 to 46.")
            continue

        displayOutputs(start, end)

        choice = input("Contimue? (Y/N) ").upper()
    return start, end

def main():
    getInputs()

if __name__ == "__main__":
    main()
# %%
