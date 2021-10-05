# Trent Brunson
# Question 2

print(
    f"Temperature Conversions\n"
    f"+++++++++++++++++++++++\n"
    f"CELSIUS       FARENHEIT\n"
    f"~~~~~~~~~~~~~~~~~~~~~~~\n"
)
c = -50
i = -50
for i in range(-50, 51, 5):
    f = (9/5) * c + 32
    print(f"   {c}\t\t{round(f)}")
    c += 5
