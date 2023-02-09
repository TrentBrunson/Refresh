def create_uteid(initials: str, num: int) -> str:
    return initials + str(num)

# create_uteid("btb", 1000)

print(create_uteid("btb", 1000))

#%%
def create_uteid(initials: str, num: int) -> str:
    return initials + str(num)
# %%
print(create_uteid("btb", 1000))

# %%
def create_uteid(initials: str, num: int) -> str:
    return f"{initials}{num}"

print(create_uteid("btb", 1000))
# %%
assert create_uteid('btb', 1000) == 'btb1001', 'ERROR: value not incremented by 1'
# %%
