num = int(input())


def f(num):
    if num == 0:
        return 0
    probably_7 = num % 10
    if probably_7 == 7:
        return 1 + f(num // 10)
    else:
        return f(num // 10)


print(f(num))
