n = int(input())


def f(n):
    if n == 0:
        return 0
    return 2 + f(n - 1)


print(f(n))
