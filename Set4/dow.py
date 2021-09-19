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

with open("data/dow.txt") as file:
    for line in file:
        currentline = line.split(',')
        tickerList.append(currentline)

# print(tickerList[0][1])

for i in range(1, 4):
    for j in range (10):
        print(f"{tickerList[(j)*i][1]}\t")
    print()
# %%
rows = []
fields = []

with open("data/dow.txt") as file:
    for row in file:
        rows.append(row)
for row in rows[:5]:
    for col in row:
        print(f"{col}\t")
    # print(tickerList)
# %%
tickerList = []

with open("data/dow.txt") as file:
    for line in file:
        currentline = line.split(',')
        tickerList.append(currentline)

print(tickerList)
# %%
