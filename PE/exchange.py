# Trent Brunson
# Question 5

#%%


#%%
def getRates():
    rates = []
    file = "exchange-rate.txt"

    with open(file) as f:
        for line in f:
            line = line.strip()
            currentLine = line.split(',')
            valuelist.append(list([currentLine[1], float(currentLine[2])]))
            keylist.append(currentLine[0])
        ratelist = dict(zip(keylist, valuelist))
    return ratelist

def getCountries():
    country1 = input("Enter name of first country: ")
    country2 = input("Enter name of second country: ")
    amount = float(input("Amount of money to convert: "))
    return country1, country2, amount

def converter(country1, country2, amount, rates):
    # us = float(rates["United States"][2])

    if country1 and country2 in rates:
        rate1 = rates[country1][1]
        # print(rate1)
        rate2 = rates[country2][1]
        # print(rate2)
        if country1 == "United States":
            conversion = amount * rate2
        elif country2 == "United States":
            conversion = amount / rate1
        else:
            conversion = amount / rate1 * rate2
        print(f"{amount:.2f} {(rates[country1][0]).lower()}s from {country1} equals "
            f"{conversion:.2f} {(rates[country2][0]).lower()}s from {country2}"
        )
    else:
        print("Please enter valid countries.")
    return

def main():
    c1, c2, money = getCountries()
    rateList = getRates()
    converter(c1, c2, money, rateList)

if __name__ == "__main__":
    main()
# %%
a = 10
b = (a)**-1
print(b)
# %%
keylist, valuelist = [], []
file = "exchange-rate.txt"

with open(file) as f:
    for line in f:
        line = line.strip()
        currentLine = line.split(',')
        valuelist.append(list([currentLine[1], float(currentLine[2])]))
        keylist.append(currentLine[0])
    ratelist = dict(zip(keylist, valuelist))
    print(ratelist)

# %%
