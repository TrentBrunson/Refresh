#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Rate of Change of Velocity Physics
# PURPOSE:    Predict parametrics of a thrown object.
# INPUT:      Starting height and velocity.
# PROCESS:    Assume object is thrown in a vacuum and that object is a spherical chicken.
#             Calculate the rate of acceleration for each second.  Display out in a table:
#             Velocity, Height, Distance Traveled, Cumulative Distance Traveled.
#             Determine apex and track time vs. height until ground impact (velocity/32sec)
#             at intervals of 0.1s.  
# OUTPUT:     Write to new file.  Display on screen. Handle exceptions.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
# %%
print(
    f"This program calculates how a spherical chicken thrown in a vacuum\n"
    f"decelerates.  It produces a table of decleration with max height achieved\n"
    f"and total time flown."
    )
height = float(input("Enter the starting height (feet): "))
velocity = float(input("Enter the initial velocity (feet/second): "))

timeToMaxHeight = velocity/32
totalDistance = t = index = 0
table = []
# {"Time":[], "height":[]}
# total time flown also equal 2 *  height

for t in range(0, int(round(timeToMaxHeight + 1))):
    hOFt = height + velocity * t - 16 * t ** 2
    totalDistance += hOFt
    # list of lists with time as the key for the output variables
    table.append([t, hOFt, totalDistance])
    t += 1
apex = apexHeight = totalDistance + height
# for item in table:
timeToFall = (2 * apex / 32) ** 0.5 # SQRT(ft / (ft/sec^2))
impactVelocity = 32 * timeToFall # (ft/sec^2 *  sec)

print(*table, apex, timeToFall, impactVelocity)

descentTable = []
# use list comprehension to step through in increments of 0.1 
# or increase everything by 10 in the range and divide the functions by 10
for time in [t/10 for t in range(0, int(round(timeToFall*10)))]:
    velocity = time * 32
    heightDelta = velocity * time
    descHeight = apexHeight-(heightDelta)
    descentTable.append([round(time,1), velocity, descHeight])
    if time.is_integer():
        table.append([time+t, round(descHeight,2), round(apex + heightDelta,2)])
    if descHeight < 0:
        break
    time += 0.1
# while apexHeight > 0:
#     apexHeight -= velocity * time
#     for time in range(0, int(round(timeToFall * 10))):
#         velocity = time * 32
#         time += 0.1
#         descentTable.append([time, velocity, apexHeight])
print(*descentTable)
print()
print(*table)
"""
Output table:
Time in seconds, height and distance traveled
"""
# %%
def chicken_up():
    """
    Time, distance and height for a spherical chicken tossed in a vacuum.
    """
    return apex

def chicken_down(startHeight, apex):
    """
    Time, distance and height for a spherical chicken tossed in a vacuum.
    """
    apex = + startHeight
    return

