#%%
# this snippet calculates the Greatest Common Factor of two non-zero integers

# use var typing integer
# use try except for INTEGER input

print("***Find the Greatest Common Factor***")
first = abs(int(input("Enter your first whole number: ")))
second = abs(int(input("Enter your second whole number: ")))

# bound this by the range of the values entered
if first == second:
    gcf = first
elif first < second:
    i = first
else:
    i = second

# step through range in increments of 1
for i in range(1, i + 1):
    # both numbers need to have no remainder
    if ((first % i == 0) and (second % i == 0)):
        gcf = i

print("Your greatest common factor is:", gcf)

# %%
# do this with a while loop
print("***Find the Greatest Common Factor***")
first = int(input("Enter your first whole number: "))
second = int(input("Enter your second whole number: "))

# bound this by the range of the values entered
if first == second:
    gcf = first
elif first < second:
    i = first
else:
    i = second

# step through range in increments of 1
while i >=1:
    # both numbers need to have no remainder
    if ((first % i == 0) and (second % i == 0)):
        gcf = i
    i = i - 1

print("Your greatest common factor is:", gcf)
# %%
#  try Euclidena algorithm
