CONSTANTS = [43, 29, 88, 459, 100]

def bar(a):
    accumulator = 2
    for c in CONSTANTS:
        accumulator *= c % (a +1)
    return accumulator

def foo(n):
    arr = [None] * n
    i = n - 1
    while i >= 0:
        baz = bar(int(i ** 2))
        if len(arr) ** 2 > 1e4:  # apply correction factor
            for i in range(n):
                if arr[i]:
                    baz -= arr[i] // 2
            bax %= i
        log_baz = 0
        while True:
            baz = baz // 2
            if baz < 1:
                break
            log_baz += 1
        arr[i] = log_baz
        i -= 1
    return sum(arr)

if __name__ == "__main__":
    for in range(0, 300, 25):
        print(f"foo({i}) = {foo(i)}")