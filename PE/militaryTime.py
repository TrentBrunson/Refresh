# Trent Brunson
# Question 3

time = []
time = str(input("Enter a military time (0000 to 2359): "))
hour = int((time[0] + time[1]))
# print(hour, type(hour))
if hour > 12:
    regHour = hour - 12
elif 0 <= hour < 1:
    regHour = hour + 12
else:
    regHour = hour

if hour >= 12:
    indicator = "p.m."
else:
    indicator = "a.m."
print(type(time))
# print(time[1])
print(f"Regular time is: {regHour}:{time[2:]} {indicator}")
