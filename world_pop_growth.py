# The world population reached 7 billion people on October 21, 2011. Assuming the world population continues to grow at 1.1% annually, 
# Provide population forecast

print(
    f"************************************************\n"
    f"This program calculates world population growth.\n"
    f"************************************************\n\n"
)

newWorldPop, worldPop = 7000000000
year = 2011

while newWorldPop < 8000000000:
    newWorldPop = newWorldPop * 1.1
    year += 1
    print(f"The population in {year} is {newWorldPop:.0f}")

print(f"The world's population will exceed 8,000,000,000 in {year}")
