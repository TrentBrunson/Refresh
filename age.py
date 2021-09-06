# check answer
def answer_check(x):
    final = x**2 - x - 1980
    return final

# %%
# figure out the age of someone when they say 
# "I will be x years old in the year x squared."
# If the birth year is 1980, at what age/in what year
# will the individual be able to make this statement?

# quadratic equation if x^2
# x = age
# x^2 = the current year
# birth year = current year - age or x^2 - x = 1980
# x^2 - x - 1980 = 0

# x = [-b +/- (b^2 - 4ac)^0.5]/2a

x = (1 + ((-1)**2 -(4 * 1 * -1980)) ** 0.5) / 2
x2 = (1 - ((-1)**2 -(4 * 1 * -1980)) ** 0.5) / 2

year = [x,x2]

# take only the positive value - no negative ages!!
answer = [i for i in year if i > 0] #list comprehension
answer, *rest = answer #extract the value from the list
answer = int(answer) 
print(answer)

# # take only the positive value - no negative ages!!  Convert list to int with lamda f(x)
# answer = list(filter(lambda yr: (yr > 0), year)) # lamda f(x)
# answer, *rest = answer
# answer = int(answer)
# print(answer)


# %%
print(f"The person born in 1980 will be {answer} year old in {1980 + answer},\n"
    f"when their age ({answer}) sqaured will be the same as the year ({1980 + answer})"
    )

# %%
