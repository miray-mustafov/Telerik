fib_cache = {}


def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_cache[n]


n = int(input())
result = fibonacci(n)
print(result)
