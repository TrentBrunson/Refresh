# Trent Brunson
# Question 5
#%%
def getRates():
    file = "exchange-rate.txt"
    valuelist, keylist = [], []

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
    if country1 and country2 in rates:
        rate1 = rates[country1][1]
        rate2 = rates[country2][1]
        if country1 == "United States":
            conversion = amount * rate2
        elif country2 == "United States":
            conversion = amount / rate1
        else:
            conversion = amount / rate1 * rate2
        print(f"{amount:,.2f} {(rates[country1][0]).lower()}s from {country1} equals "
            f"{conversion:,.2f} {(rates[country2][0]).lower()}s from {country2}"
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
# this time with a list
def getRates():
    file = "exchange-rate.txt"
    currencylist, valuelist, keylist = [], [], []
    with open(file) as f:
        for line in f:
            line = line.strip()
            currentLine = line.split(',')
            valuelist.append(currentLine[1])
            currencylist.append(float(currentLine[2]))
            keylist.append(currentLine[0])
        ratelist = list(zip(keylist, valuelist, currencylist))
        print(ratelist)
    return ratelist

def getCountries():
    country1 = input("Enter name of first country: ")
    country2 = input("Enter name of second country: ")
    amount = float(input("Amount of money to convert: "))
    return country1, country2, amount

def converter(country1, country2, amount, rates):
    ratesDict = {} # have to convert to dictionary to reference index; just passed f(x) as list
    # for row in rates:
    for row in range (len(rates)):
        ratesDict[rates[row][0]] = [rates[row][1], rates[row][2]]
    rate1 = ratesDict[country1][1]
    rate2 = ratesDict[country2][1]
    if country1 == "United States":
        conversion = amount * rate2
    elif country2 == "United States":
        conversion = amount / rate1
    else:
        conversion = amount / rate1 * rate2
    print(f"{amount:.2f} {(ratesDict[country1][0]).lower()}s from {country1} equals "
        f"{conversion:.2f} {(ratesDict[country2][0]).lower()}s from {country2}"
    )
    return

def main():
    c1, c2, money = getCountries()
    rateList = getRates()
    print(type(rateList))
    converter(c1, c2, money, rateList)

if __name__ == "__main__":
    main()
# %%