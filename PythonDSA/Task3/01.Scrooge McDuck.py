def solution(matrix):
    def cell_valid(r, c):
        if r <= -1 or r >= n:
            return False
        if c <= -1 or c >= m:
            return False
        if matrix[r][c] == 0:
            return False
        return True

    r, c, coins = start_r, start_c, 0

    while True:
        next_cell = [0, None, None]  # [cur_max_val, r, c]
        if cell_valid(r, c - 1):  # left
            next_c = c - 1
            if matrix[r][next_c] > next_cell[0]:
                next_cell[0], next_cell[1], next_cell[2] = matrix[r][next_c], r, next_c
        if cell_valid(r, c + 1):  # right
            next_c = c + 1
            if matrix[r][next_c] > next_cell[0]:
                next_cell[0], next_cell[1], next_cell[2] = matrix[r][next_c], r, next_c
        if cell_valid(r - 1, c):  # up
            next_r = r - 1
            if matrix[next_r][c] > next_cell[0]:
                next_cell[0], next_cell[1], next_cell[2] = matrix[next_r][c], next_r, c
        if cell_valid(r + 1, c):  # down
            next_r = r + 1
            if matrix[next_r][c] > next_cell[0]:
                next_cell[0], next_cell[1], next_cell[2] = matrix[next_r][c], next_r, c

        if not next_cell[0]:
            break

        r, c, coins = next_cell[1], next_cell[2], coins + 1
        matrix[r][c] -= 1

    return coins


def find_zero_col(row):
    for c, num in enumerate(row):
        if num == 0:
            return c


n, m = map(int, input().split())
matrix = []
start_r, start_c = None, None
for r in range(n):  # build the matrix and serach for zero at the same time
    row = list(map(int, input().split()))
    if start_c is None:
        start_r, start_c = r, find_zero_col(row)
    matrix.append(row)

print(solution(matrix))

"""
4 3
3 2 4
2 0 3
1 1 5
2 2 5
"""
