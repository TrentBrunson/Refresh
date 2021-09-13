#%%
#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Weight Converter
# PURPOSE:    Print a table for a predefined range converting pounds to kilos.
# INPUT:      none
# PROCESS:    Iterate through a range and append the conversions to a list.
# OUTPUT:     Print the list.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# this snippet converts pounds to kilos for a given range in increments of 10 pounds

startWeight = 100
endWeight = 300
weightTable = {}

for startWeight in range(startWeight, endWeight + 10, 10):
    weightTable[startWeight] = round(startWeight/2.2046, 3)

print(
    f"This is a weight conversion table for pounds to kilos (100-300lbs):\n\n"
    f"Pounds\tKilos"
)
for key, value in weightTable.items():
    print(
        f"{key}\t"
        f"{value}"
    )

# list comprehension printing
# [print(key,"\t",value) for key, value in weightTable.items()]
#%%
# bonus ask for input on which way to switch

weights = []

for weight in range(100, 300 + 10, 10):
        weights.append(weight)

for weight in weights:
    print("Lbs: " + str(weight).ljust(5) + " Kg: " + str(round( (weight / 2.2046), 2) ).ljust(8))
# %%
# A dictionary of student names and their score
student_score = {   'Ritika': 5,
                    'Sam': 7, 
                    'John': 10, 
                    'Aadi': 8}
# Iterate over the key-value pairs of a dictionary 
# using list comprehension and print them
[print(key,':',value) for key, value in student_score.items()]
# %%
