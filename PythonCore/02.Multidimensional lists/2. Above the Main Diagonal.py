n = int(input())
res, start, end = 0, 1, n
while start < end:
    for power in range(start, end):
        res += 2 ** power
    start += 2
    end += 1
print(res)