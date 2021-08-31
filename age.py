# figure out the age of someone when they say "I will be x years old in the year x squared.

# x = age
# x^2 = the current year
# birth year = current year - age or x^2 - x = 1980
# x^2 - x - 1980 = 0

# x = [-b +/- (b^2 - 4ac)^0.5]/2a

#%%

x = (1 + ((-1)**2 -(4 * 1 * -1980)) ** 0.5) / 2
x2 = (1 - ((-1)**2 -(4 * 1 * -1980)) ** 0.5) / 2
print(x)
print(x2)
# %%
# b^2 - 4ac
x2 = (-1)**2 -(4 * 1 * -1980)
print(x2)

# %%
