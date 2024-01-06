n = int(input())
m = [[0] * n for _ in range(n)]  # initialize matrix
num, center_number = 1, n * n

start, end = 0, n
while num <= center_number:
    for c in range(start, end):  # top row iteration
        m[start][c], num = num, num + 1
    for r in range(start + 1, end):  # rightmost column iteration
        m[r][end - 1], num = num, num + 1

    for c in range(end - 2, start - 1, -1):  # bottom row
        m[end - 1][c], num = num, num + 1
    for r in range(end - 2, start, -1):  # leftmost column
        m[r][start], num = num, num + 1

    start, end = start + 1, end - 1

for row in m:
    print(*row)
