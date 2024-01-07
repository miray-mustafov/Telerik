def bounce(N, M):
    matrix = [[2 ** (i + j) for j in range(M)] for i in range(N)]
    total = 0
    r, c = 0, 0
    dir_r, dir_c = 1, 1
    while 0 <= r < N and 0 <= c < M:
        total += matrix[r][c]
        if r + dir_r < 0 or r + dir_r >= N:
            dir_r *= -1
        elif c + dir_c < 0 or c + dir_c >= M:
            dir_c *= -1
        r += dir_r
        c += dir_c
    return total


N, M = map(int, input().split())
result = bounce(N, M)
print(result)

# def make_matrix_pow2(rows, cols):
#     matrix = []
#     for power in range(rows):
#         row = []
#         for cur_power in range(power, cols + power):
#             row.append(2 ** cur_power)
#         matrix.append(row)
#     return matrix
#
#
# def is_corner(r, c, rows, cols):
#     if (r + 1 >= rows and c + 1 >= cols
#             or r + 1 >= rows and c - 1 < 0
#             or r - 1 < 0 and c + 1 >= cols
#             or r - 1 < 0 and c - 1 < 0):
#         return True
#     return False
#
#
# def change_direction(r, c, dr, dc, rows, cols):  # todo
#     if dr == 1 and dc == 1:  # left \ right
#         if r == rows - 1:  # check for floor hit
#             dr = -dr
#         else:
#             dc = -dc
#     elif dr == -1 and dc == 1:  # left / right
#         if r == 0:  # ceiling hit
#             dr = -dr  # =>  we go down-right
#         else:
#             dc = -dc
#     elif dr == 1 and dc == -1:  # right / left
#         if r == rows - 1:
#             dr = -dr
#         else:
#             dc = -dc
#     elif dr == -1 and dc == -1:  # right \ left
#         if r == 0:  # check for ceiling hit
#             dr = -dr
#         else:
#             dc = -dc
#     return dr, dc
#
#
# rows, cols = map(int, input().split())
# matrix = make_matrix_pow2(rows, cols)
# res = matrix[0][0]
# r = c = 0
# dr = dc = 1
# while True:
#     if 0 <= r + dr < rows and 0 <= c + dc < cols:  # check if next step is in bounds
#         step = matrix[r + dr][c + dc]
#         r, c = r + dr, c + dc
#         res += step
#     else:
#         if is_corner(r, c, rows, cols):
#             break
#         dr, dc = change_direction(r, c, dr, dc, rows, cols)
#
# print(res)


''' inputs, results
3 4 , 49 | 3 6, 209
4 3, 49 | 6 3, 209
'''
