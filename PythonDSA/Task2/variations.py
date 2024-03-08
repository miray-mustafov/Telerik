def f(z, x, y, prefix=''):
    if z == 0:
        print(prefix)
        return
    f(z - 1, x, y, prefix + x)
    f(z - 1, x, y, prefix + y)


z = int(input())
x, y = input().split()
if ord(y) < ord(x):
    x, y = y, x
f(z, x, y)
