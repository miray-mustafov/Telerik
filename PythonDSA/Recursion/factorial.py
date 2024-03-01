n = int(input())


def F(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    return n * F(n - 1)


print(F(n))
