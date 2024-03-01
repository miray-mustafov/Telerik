num = int(input())


def f(num, suma):
    if num < 10:
        return num
    suma += f(num // 10, suma) + num % 10
    return suma


print(f(num, 0))
# second----------------------------------
num = int(input())


def f(num):
    if num < 10:
        return num
    return f(num // 10) + num % 10


print(f(num))
