#!/usr/bin/env python3

# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Triathlon fuel consumption
# PURPOSE:    This will return how many calories are burned (& weight lost) for a trio of exercises. 
# INPUT:      Times for each of 3 activities: swim, bike & run.
# PROCESS:    Use given values for caloric burn per activity.
# OUTPUT:     Caloried burned and weight lost.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.
"""
In 2014, China's population was 1.37 billion, growing at a rate of 0.51% per year.  Likewise,
India's poulation was 1.26 billion, growing at a rate of 1.35% per year.

This program assumes growth rates remain the same and calculates when India's population 
will exceed China's.
"""

chinaPop = 1370000000
indiaPop = 1260000000
year = 2014

print(
    f"Year:             {year}\n"
    f"China's population: {chinaPop:,.0f}\n"
    f"India's population: {indiaPop:,.0f}\n\n"
)

while indiaPop <= chinaPop:
    indiaPop = indiaPop * 1.0135
    chinaPop = chinaPop * 1.0051
    year += 1
    print(
        f"Year:             {year}\n"
        f"China's population: {chinaPop:,.0f}\n"
        f"India's population: {indiaPop:,.0f}\n\n"
    )

print(
    f"In the year {year}, India's population ({indiaPop:,.0f}) will exceed China's population ({chinaPop:,.0f}).\n\n"
)