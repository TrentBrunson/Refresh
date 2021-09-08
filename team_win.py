# User input favorite team, games won, and number of games lost last season. 
# Display team name and the percentage of games won. 

teamName = input("What is the name of your favorite team? ")
print()
teamWins = int(input("How many games have they won? "))
print()
teamLosses = int(input("How many games have the lost? "))
print()

print(f"The {teamName} had a winning percentage of {(teamWins / (teamWins + teamLosses)) * 100:.1f}%.")
