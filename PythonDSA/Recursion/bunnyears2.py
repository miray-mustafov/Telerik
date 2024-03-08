n = int(input())


def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 3 + f(n - 1)
    else:
        return 2 + f(n - 1)


print(f(n))
