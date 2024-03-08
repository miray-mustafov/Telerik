num = int(input())


def f(num):
    if num == 0:
        return 0
    if num % 10 == 7:
        return 1 + f(num // 10)
    return f(num // 10)


print(f(num))
