def solution():
    n, arr = int(input()), []
    for _ in range(n):  # initializing the arr
        arr.append(input())

    if n == 1: return 1

    l = r = max_equal_sequence = 0
    while r < n:
        if arr[l] != arr[r]:
            max_equal_sequence = max(max_equal_sequence, r - l)
            l = r
        r += 1
    return max(max_equal_sequence, r - l)


print(solution())
