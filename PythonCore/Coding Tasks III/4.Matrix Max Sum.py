n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

nums = input().split()
pairs = []
for i in range(1, len(nums), 2):
    r = int(nums[i - 1])
    c = int(nums[i])
    pairs.append([r, c])


def solution(matrix, n, pairs):
    max_sum = float('-inf')
    for row, col in pairs:
        if row > 0:
            start_c, end_c = 0, abs(col)
        else:
            start_c, end_c = abs(col) - 1, len(matrix[0])

        if col > 0:
            start_r, end_r = 0, abs(row) - 1
        else:
            start_r, end_r = abs(row), len(matrix)

        cur_sum = 0
        for c in range(start_c, end_c):
            cur_sum += matrix[abs(row) - 1][c]
        for r in range(start_r, end_r):
            cur_sum += matrix[r][abs(col) - 1]

        max_sum = max(max_sum, cur_sum)

    return max_sum


print(solution(matrix, n, pairs))
'''
5
1 22 3 41 5 2
2 13 4 -5 6 5
-6 5 9 31 2 8
3 14 5 -6 7 4
4 -5 6 -7 8 7
2 3 -4 5
'''