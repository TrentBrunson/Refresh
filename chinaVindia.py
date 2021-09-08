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