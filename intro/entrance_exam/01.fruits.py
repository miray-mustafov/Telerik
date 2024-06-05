n = int(input())
oranges = 0
apples = 0
for k in range(1, n + 1):
    if k % 2 == 0:
        oranges += k * k
    else:
        apples += k * k

print(oranges - apples)
