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
roseWins = []
file = "data/Rosebowl.txt"

with open(file) as f:
    for line in f:
        line = line.strip()
        roseWins.append(line)

winDict = {}
for i in range(len(roseWins)):
    team = roseWins[i]
    count = 0
    for j in range(i, len(roseWins)):
        if roseWins[j] == roseWins[i]:
            count += 1
    winCount = {team:count}
    if team not in winDict.keys():
        winDict.update(winCount)

# find teams with 4 or more wins
win4 = {k:v for (k,v) in winDict.items() if v >= 4}
sortedWins = sorted(win4.items(), reverse=True, key = lambda kv:kv[1])

# print(*sortedWins)
print(
    f"Teams with more than 4 wins at the Rose Bowl:\n"
    f"Team\t\t    Wins"
)

for team in win4:
    print(f"{team:<20}{win4[team]:<20}")

with open("data/Rosewinners.txt", "w") as newF:
    for k, v in winDict.items():
        newF.writelines(f"{k},{v}\n")
# %%
from typing import Counter

roseWins = []
file = "data/Rosebowl.txt"

with open(file) as f:
    for line in f:
        line = line.strip()
        roseWins.append(line)

# use Counter method from typing module
wins = Counter(roseWins)
print(wins)

winDict = {}
for i in range(len(roseWins)):
    team = roseWins[i]
    count = 0
    for j in range(i, len(roseWins)):
        if roseWins[j] == roseWins[i]:
            count += 1
    winCount = {team:count}
    if team not in winDict.keys():
        winDict.update(winCount)

# find teams with 4 or more wins using dict comprehension
win4 = {k:v for (k,v) in winDict.items() if v >= 4}
print(win4)

winner = list(win4.keys())
winner.sort(reverse=True)

for team in win4.keys():
    print(f"{team}\t\t{winDict[team]}")

print(sorted(win4.items(), reverse=True, key = lambda kv:kv[1]))
# %%
def read_file_to_list():
    roses = []
    file = "data/Rosebowl.txt"

    with open(file) as f:
        for line in f:
            line = line.strip()
            roses.append(line)
    return roses

def win_counter(roseWins):
    winDict = {}
    for i in range(len(roseWins)):
        team = roseWins[i]
        count = 0
        for j in range(i, len(roseWins)):
            if roseWins[j] == roseWins[i]:
                count += 1
        winCount = {team:count}
        if team not in winDict.keys():
            winDict.update(winCount)
    # find teams with 4 or more wins
    win4 = {k:v for (k,v) in winDict.items() if v >= 4}
    # make dictionary into list so it prints nicer
    # sort by values then keys; need staged sort to reverse sort for the key column
    sortedWins = dict(sorted(win4.items(), reverse=True, key = lambda kv:(kv[1],kv[0])))
    return team, sortedWins

def results_output(team, sortedWinsDict):
    print(
        f"Teams with more than 4 wins at the Rose Bowl:\n"
        f"Team\t\t    Wins"
    )

    for team in sortedWinsDict:
        print(f"{team:<20}{sortedWinsDict[team]:<20}")

    with open("data/Rosewinners.csv", "w") as newF:
        for k, v in sortedWinsDict.items():
            newF.writelines(f"{k},{v}\n")

def main():
    roseWinners = read_file_to_list()
    teams, wins = win_counter(roseWinners)
    results_output(teams, wins)

if __name__ == "__main__":
    main()
# %%
