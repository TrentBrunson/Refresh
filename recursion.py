# %%
n = 2
def recur_fx(n):
    if n == 6:
        return n
    else:
        return 3 + recur_fx(n +1)
print(recur_fx(n))

# %%
def add_numbers(upper):
    if upper == 0:
        return upper
    else:
        print(upper)
        return upper + add_numbers(upper -1)

def main():
    total = add_numbers(5)
    print(total)

main()
# %%
# fibonacci

def fib(n):
    if n == 0:  # base case
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + +fib(n-2)

for i in range(44):
    print(fib(i), end = ", ")

'''
fibonacci for 44:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 
196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 
9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 
165580141, 267914296, 433494437

took ~ 2 minutes
'''
# %%
# iterative fibonacii
n = 44

def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n1 = 0
    n2 = 1
    fib = 0
    for i in range(2, n+1):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    return fib

for i in range(n):
    print(fib_iter(i), end = ", ")
'''
same result as above but in less than 1 second
'''
# %%
