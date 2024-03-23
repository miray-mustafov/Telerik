def solution(matrix):
    def cell_valid(r, c, num):
        if r < 0 or r >= n or c < 0 or c >= m:
            return False
        return matrix[r][c] == num

    def dfs(r, c, num):
        if (r, c) in visited[num]:
            return 0
        visited[num].add((r, c))
        count = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if cell_valid(nr, nc, num):
                count += dfs(nr, nc, num)
        return count

    visited = {}  # keep visited cells for each num
    result = 0
    for r in range(n):
        for c in range(m):
            num = matrix[r][c]
            if num not in visited:
                visited[num] = set()
            result = max(result, dfs(r, c, num))
    return result


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
print(solution(matrix))
# Example Input:
# 5 6
# 1 3 2 2 2 4
# 3 3 3 2 4 4
# 4 3 1 2 3 3
# 4 1 1 3 3 1
# 4 3 3 3 1 1
# Output:
# 7


# """
# Constraint:
# 3 <= N, M <= 1024
# Example Input:
# 5 6
# 1 3 2 2 2 4
# 3 3 3 2 4 4
# 4 3 1 2 3 3
# 4 1 1 3 3 1
# 4 3 3 3 1 1
# Output:
# 7
# """
#
#
# def solution(matrix):
#     def cell_valid(r, c):
#         if r <= -1 or r >= n:
#             return False
#         if c <= -1 or c >= m:
#             return False
#         if matrix[r][c] != num:
#             return False
#         return True
#
#     def dfs(r, c):
#         count = 0
#         next_rc = (r - 1, c)  # up
#         if cell_valid(*next_rc):
#             if next_rc not in nums_d[num]:
#                 nums_d[num].add(next_rc)
#                 count += 1 + dfs(*next_rc)
#             else:
#                 count += 0 + dfs(*next_rc)
#
#         next_rc = (r, c - 1)  # left
#         if cell_valid(*next_rc):
#             if next_rc not in nums_d[num]:
#                 nums_d[num].add(next_rc)
#                 count += 1 + dfs(*next_rc)
#             else:
#                 count += 0 + dfs(*next_rc)
#
#         next_rc = (r, c + 1)  # right
#         if cell_valid(*next_rc):
#             if next_rc not in nums_d[num]:
#                 nums_d[num].add(next_rc)
#                 count += 1 + dfs(*next_rc)
#             else:
#                 count += 0 + dfs(*next_rc)
#
#         next_rc = (r + 1, c)  # down
#         if cell_valid(*next_rc):
#             if next_rc not in nums_d[num]:
#                 nums_d[num].add(next_rc)
#                 count += 1 + dfs(*next_rc)
#             else:
#                 count += 0 + dfs(*next_rc)
#
#         return 1 + count
#
#     nums_d, res = {}, 0  # keeps track of the visited numbers
#     for r in range(n):
#         for c in range(m):
#             num = matrix[r][c]
#             if num not in nums_d:
#                 nums_d[num] = {(r, c)}
#                 res = max(res, dfs(r, c))
#             elif (r, c) not in nums_d[num]:  # means this is separated path with same num
#                 nums_d[num].add((r, c))
#                 # todo dfs
#
#
# n, m = map(int, input().split())
# matrix = []
# for _ in range(n):
#     matrix.append(input().split())
# print(solution(matrix))
