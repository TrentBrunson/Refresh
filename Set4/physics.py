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
from os import write


print(
    f"This program calculates how a spherical chicken thrown upwards in a vacuum\n"
    f"decelerates.  It produces a table of decleration with max height achieved\n"
    f"and total time flown."
    )
height = float(input("Enter the starting height (feet): "))
velocity = float(input("Enter the initial velocity (feet/second): "))

timeToMaxHeight = velocity/32
totalDistance = t = 0
table = []
# {"Time":[], "height":[]}
# total time flown also equal 2 *  height

for t in range(0, int(round(timeToMaxHeight + 1))):
    hOFt = height + velocity * t - 16 * t ** 2
    # totalDistance += hOFt
    # list of lists with time as the key for the output variables
    table.append([t, hOFt, hOFt])
    t += 1
apex = apexHeight = hOFt + height
# for item in table:
timeToFall = (2 * apex / 32) ** 0.5 # SQRT(ft / (ft/sec^2))
impactVelocity = 32 * timeToFall # (ft/sec^2 *  sec)

print(*table, "\n\n", "apex: ", apex, " --time to fall: ", timeToFall, " --impact velocity", impactVelocity, "\n")

descentTable = []
# use list comprehension to step through in increments of 0.1 
# or increase everything by 10 in the range and divide the functions by 10
for time in [t/10 for t in range(0, int(round(timeToFall*10)))]:
    heightDelta = (time ** 2) * 32
    descHeight = apexHeight-(heightDelta)
    descentTable.append([round(time,1), descHeight, heightDelta])
    # only add whole seconds to table as to not have different units of output
    if time.is_integer():
        table.append([time+t, round(descHeight,2), round(apex + heightDelta,2)])
    if descHeight < 0:
        break
    time += 0.1

print(*descentTable)
print("\n\n")
print(*table)
"""
Output table:
Time in seconds, height and distance traveled
"""
print(f"{'Time':<10}{'Actual Height':<20}{'Total Distance':<20}")
for i in range(len(table)):
    print(f"{int(table[i][0]):<10}{table[i][1]:<20}{table[i][2]:<20}")
print(f"Your starting parameters:\nHeight: {height} feet\nStarting velocity: {velocity} ft/sec"
    f"\n\nTotal time: {round(time + timeToFall,3)} seconds, Apex: {apex} feet, "
    f"Total distance traveled: {2*apex} feet"
)
# **********************************************************************************
# **********************************************************************************
# %%
def get_params():
    print(
    f"This program calculates how a spherical chicken thrown upwards in a vacuum\n"
    f"decelerates.  It produces a table of decleration with max height achieved\n"
    f"and total time flown."
    )
    height = float(input("Enter the starting height (feet): "))
    velocity = float(input("Enter the initial velocity (feet/second): "))
    return height, velocity

def physics_check(apex):
    # total time flown also equal 2 * height plus doubled starting height
    timeToFall = (2 * apex / 32) ** 0.5 # SQRT(ft / (ft/sec^2))
    impactVelocity = 32 * timeToFall # (ft/sec^2 *  sec)
    return timeToFall, impactVelocity

def chicken_up(startH, startV):
    """
    Calculate time, distance and height for a spherical chicken tossed upwards in a vacuum.
    """
    timeToMaxHeight = startV/32
    t = 0
    tableUp = []
    
    for t in range(0, int(round(timeToMaxHeight + 1))):
        # formula for height of an object at a given time under a constant
        # force of deceleration and an initial starting velocity
        hOFt = startH + startV * t - 16 * t ** 2
        # list of lists with time as the key for the output variables
        # second height for capturing total distance in the descent table
        tableUp.append([t, hOFt, hOFt])
        t += 1
    apex = hOFt + startH
    return apex, tableUp

def chicken_down(crest, finaltable, ttf):
    """
    Time, distance and height for a spherical chicken falling in a vacuum.
    """
    t = 0
    tableDown = []
    # use list comprehension to step through in increments of 0.1 
    # or increase everything by 10 in the range and divide the functions by 10
    for time in [t/10 for t in range(0, int(round(ttf*10)))]:
        velocity = time * 32
        heightDelta = velocity * time
        descHeight = crest-(heightDelta)
        tableDown.append([round(time,1), velocity, descHeight])
        # only add whole seconds to table as to not have different units of output
        if time.is_integer(): 
            finaltable.append([time+t, round(descHeight,2), round(crest + heightDelta,2)])
        if descHeight < 0:
            break
        time += 0.1
    # print(*tableDown)
    return finaltable, time

def outputs(table, height, velocity, apex, time, fallTime):
    print(f"{'Time':<10}{'Actual Height':<20}{'Total Distance':<20}")
    for i in range(len(table)):
        print(f"{int(table[i][0]):<10}{table[i][1]:<20}{table[i][2]:<20}")
    print(f"Your starting parameters:\nHeight: {height} feet\nStarting velocity: {velocity} ft/sec"
        f"\n\nTotal time: {round(time + fallTime,3)} seconds, Apex: {apex} feet, "
        f"Total distance traveled: {2*apex} feet"
        )
    
    with open("object-trajectory.txt", "w") as f:
        f.writelines(f"Your starting parameters:\nHeight: {height} feet\nStarting velocity: {velocity} ft/sec\n")
        f.writelines(f"{'Time':<15}{'Actual Height':<15}{'Total Distance':<15}\n")
        # for line in table:
        for row in table:
            for field in row:
                f.writelines(f"{field:<15}")
            f.writelines("\n")        
        f.write(f"Total time: {round(time + fallTime,3)} seconds, Apex: {apex} feet, "
            f"Total distance traveled: {2*apex} feet"
            )
    with open("o2.txt", "w") as newF:
        for row in table:
            for field in row:
                newF.writelines(f"{field},")
            newF.writelines("\n")
def main():
    ht, vel = get_params()
    peak, upTable = chicken_up(ht, vel)
    tof, impactV = physics_check(peak)
    fTable, time = chicken_down(peak, upTable, tof)
    outputs(fTable, ht, vel, peak, time, tof)

if __name__ == "__main__":
    main()
# %%
