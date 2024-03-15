def dfs(matrix, i, j, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0 or visited[i][j]:
        return 0

    visited[i][j] = True
    size = 1

    size += dfs(matrix, i + 1, j, visited)
    size += dfs(matrix, i - 1, j, visited)
    size += dfs(matrix, i, j + 1, visited)
    size += dfs(matrix, i, j - 1, visited)

    return size


def conquer_sizes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False] * m for _ in range(n)]
    sizes = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                sizes.append(dfs(matrix, i, j, visited))

    sizes.sort(reverse=True)
    return sizes


n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
sizes = conquer_sizes(matrix)
for s in sizes:
    print(s)
