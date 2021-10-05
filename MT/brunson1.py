# Trent Brunson
# Question 1
startingSalary = float(input("Enter the beginning salary: "))
newSalary = startingSalary
i = 0
for i in range(3):
    newSalary = newSalary * 1.05
    # print(newSalary) - code check

print(f"New salary: ${newSalary:.2f}\n"
    f"Change: {(newSalary/startingSalary - 1)*100:.2f}%"
)