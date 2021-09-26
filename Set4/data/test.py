# PYHW 4
# Part 1 - read and count Rose Bowl winners
winners = {}

# Establishing Dictionary
def populate_dict(file_name):
  with open(file_name) as f:
    for line in f:
        # Remove leading & trailing characters
      team = line.strip()

      # Incrementing winners count or adding if doesn't exist
      if team in winners:
        winners[team] += 1
      else:
        winners[team] = 1

# Creating dictionary with team, count  
populate_dict("Rosebowl.txt")

print ("TOTAL count of Rose Bowl wins / by team (from 1902 to 2020)")
print ("")
# Sorting most wins first
sorted = dict(sorted(winners.items(), key=lambda item: item[1], reverse=True))

count = 0
for key in sorted.keys():
    print(key + " " + str(sorted[key]))

# Part 2 - creating the CSV

import csv

winners = {}

def populate_dict(file_name):
  with open(file_name) as f:
    for line in f:
      team = line.strip()

      # Incrementing winners count or adding if doesn't exist
      if team in winners:
        winners[team] += 1
      else:
        winners[team] = 1

# Creating dictionary with team, count  
populate_dict("Rosebowl.txt")

# Sorting most wins first
sorted = dict(sorted(winners.items(), key=lambda item: item[1], reverse=True))

with open('Rosebowl.csv', 'w') as csv_file:
  for key in sorted.keys():

    # write to csv here
    csv_file.writelines(key + "," + str(sorted[key]) + "\n")




# Part 3 - Teams who have won more than 4 Rose Bowls

import csv

winners = {}

def populate_dict(file_name):
  with open(file_name) as f:
    for line in f:
      team = line.strip()

      # Incrementing winners count or adding if doesn't exist
      if team in winners:
        winners[team] += 1
      else:
        winners[team] = 1

# Creating dictionary with team, count  
populate_dict("Rosebowl.txt")

# Sorting most wins first
sorted = dict(sorted(winners.items(), key=lambda item: item[1], reverse=True))

total = 5
count = 0

with open('Rosebowl.csv', 'w') as csv_file:
  for key in sorted.keys():

    # write to csv here
    csv_file.writelines(key + "," + str(sorted[key]) + "\n")

    if count <= total:
      print(key + " " + str(sorted[key]))
      count += 1