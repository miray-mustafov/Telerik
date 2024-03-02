def f(arr, index):
    if index >= len(arr):
        return 0

    if arr[index] == 11:
        return 1 + f(arr, index + 1)

    return f(arr, index + 1)


arr = list(map(int, input().split(',')))
index = int(input())
print(f(arr, index))
