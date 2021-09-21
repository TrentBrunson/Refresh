#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Rose Bowl Winners
# PURPOSE:    Extract values from file and display number of wins by school.
# INPUT:      File with name data and user selection.
# PROCESS:    Import data file.  Get user input.  If extant, report back to user.
#             If not found, add to file and report insertion completed.  
#             Write to new file.  Handle exceptions.
# OUTPUT:     Report to user on screen and create new file with new names.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
# %%
from typing import Counter

roses = []
file = "data/Rosebowl.txt"

with open(file) as f:
    for line in f:
        line = line.strip()
        roses.append(line)

# print(roses)

# use Counter method from typing module
wins = Counter(roses)
print(wins)

winDict = {}
for i in range(len(roses)):
    team = roses[i]
    count = 0
    for j in range(i, len(roses)):
        if roses[j] == roses[i]:
            count += 1
    winCount = {team:count}
    if team not in winDict.keys():
        winDict.update(winCount)

print(sorted(winDict, reverse=True))
print(winDict)

win4 = {k:v for (k,v) in winDict.items() if v >= 4}
print(win4)
# %%
from typing import Counter

roses = []
file = "data/Rosebowl.txt"

with open(file) as f:
    for line in f:
        line = line.strip()
        roses.append(line)

# print(roses)

# use Counter method from typing module
wins = Counter(roses)
print(wins)

winDict = {}
for i in range(len(roses)):
    team = roses[i]
    count = 0
    for j in range(i, len(roses)):
        if roses[j] == roses[i]:
            count += 1
    winCount = {team:count}
    if team not in winDict.keys():
        winDict.update(winCount)

print(sorted(winDict, reverse=True))
print(winDict)

win4 = {k:v for (k,v) in winDict.items() if v >= 4}
print(win4)
# %%
