#%%
# this snippet converts pounds to kilos for a given range in increments of 10 pounds

startWeight = 100
endWeight = 300
weightTable = {}

for startWeight in range(startWeight, endWeight + 10, 10):
    weightTable[startWeight] = startWeight/2.2046

print(weightTable)
#%%
# bonus ask for input on which way to switch