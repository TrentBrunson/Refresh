#!/usr/bin/env python3

# light bulb #6
'''
1, 2,3, & 6 - leaves light off

#9: 1, 3, 9 - leaves light on

if odd number of people touch switch, light is on; if even number touch it, it ends of being off

count the number of factors / 2, MOD of 1 says

only perfect squares have odd number of factors
'''


"""
"""
#%%
lightArray = {}
i = 0
for i in range(1, 1001):
    if i % 2 == 0:
        lightArray.append{i, "off"}
# %%
lightArray = {}
i = 0

# load initial dictionary with run 1
while i < 1000:
    lightArray.update({i+1:"on"})
    i+=1

# print(lightArray)
i = 1
for i in range(1,len(lightArray)):
    j = i
    for j in range(j, len(lightArray)):
        if i % j == 0:
            if lightArray.values() == "on":
                switch = {j, 'off'}
                lightArray.update(switch)
            else:
                switch = {j, 'on'}
                lightArray.update(switch)
        else: continue

# %%
testDict = {}

a = input("on or off: ")
b ={1:a}
testDict.update(b)
print(testDict)
# %%
