#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Palindrome
# PURPOSE:    Identify if the two inputs meet the criteria of a palindrome.
# INPUT:      User input two strings of words or phrases.
# PROCESS:    Strip puntucation and spaces.  Reverse order of second input and compare.
# OUTPUT:     If true, display acknowledgement that inputs are a palindrome, otherwise, no.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

"""
Write a program that displays the stock symbol for all 30 companies in a 3 X 10 table. 
Ask the user to enter a symbol and then display the details for that company. 
The sample output for one user session is as follows:

Symbols for the Thirty DOW Stocks
AXP      BA       CAT      CSCO     CVX      DD       DIS      GE       GS       HD
IBM      INTC     JNJ      JPM      KO       MCD      MMM      MRK      MSFT     NKE
PFE      PG       T        TRV      UNH      UTX      V        VZ       WMT      XOM      

Enter a symbol: MCD
Company: McDonald's
Industry: Fast food
Exchange: NYSE
Growth in 2013: 10.00%
Price/Earnings ratio in 2013: 17.48
"""
#%%
# iterate through rows of txt file and print to screen

tickerList = []
tickerSymbol = []
DOWdict = {}
choice = "Y"

with open("data/dow.txt") as file:
    for line in file:
        currentLine = line.split(',')
        tickerList.append(currentLine)

for i in range(30):
    tickerSymbol.append(tickerList[i][1]) 

while choice.upper() == "Y":
    print("Symbols for the Thirty DOW Stocks")
    print(*tickerSymbol[:10], sep="\t")
    print(*tickerSymbol[10:20], sep="\t")
    print(*tickerSymbol[-10:], sep="\t")
    print()

    DOWdict = dict(zip(tickerSymbol, tickerList))

    try:
        company = str(input("Enter a symbol: ").upper())
    except ValueError:
        print("Only enter ticker symbols.\n\n")
        continue
    if company.upper() == "EXIT":
        break
    elif company in tickerSymbol:
        print(
            f"Enter a symbol: {company}\n"
            f"Company: {DOWdict[company][0]}\n"
            f"Industry: {DOWdict[company][3]}\n"
            f"Exhange: {DOWdict[company][2]}\n"
            f"Growth in 2013: {((float(DOWdict[company][5])/float(DOWdict[company][4]))-1) * 100:.2f}%\n"
            f"Price/Earnings ratio in 2013: {float(DOWdict[company][5])/float(DOWdict[company][6]):.2f}\n"
        )
    else:
        print("Only enter ticker symbols from the menu.\n\n")
        continue
    choice = input("Would you like to make another selection? (Y/N) ")
# %%
