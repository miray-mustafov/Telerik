num = int(input())


def f(num):
    if num == 0:
        return 0

    if num % 10 == 8:
        if (num // 10) % 10 == 8:
            return 2 + f(num // 10)
        return 1 + f(num // 10)
    return f(num // 10)


print(f(num))
