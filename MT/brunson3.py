# Trent Brunson
# Question 3

shortColor = []
file = "MT\colors.txt"
with open(file) as f:
    for line in f:
        line = line.strip()
        if len(line) < 7:
            shortColor.append(line)

with open("ShortColors.txt", "w") as newF:
        for line in shortColor:
            newF.writelines(f"{line}\n")