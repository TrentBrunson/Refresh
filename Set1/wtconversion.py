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
    weightTable[startWeight] = startWeight/2.2046

print(weightTable)
#%%
# bonus ask for input on which way to switch

weights = []

for weight in range(100, 300):
    if weight % 10 == 0:
        weights.append(weight)

for weight in weights:
    print("Lbs: " + str(weight).ljust(5) + " Kg: " + str(round( (weight / 2.2046), 2) ).ljust(8))
# %%
