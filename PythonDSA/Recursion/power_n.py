base = int(input())
n = int(input())


def f(base, n):
    if n == 1:
        return base
    elif n == 0:
        return 1
    return base * f(base, n - 1)


print(f(base, n))
