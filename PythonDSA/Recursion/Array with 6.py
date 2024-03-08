def array_contains_6(arr, index):
    if index > len(arr):
        return 'false'
    if arr[index] == 6:
        return 'true'
    return array_contains_6(arr, index + 1)


arr = input()
index = int(input())
print(array_contains_6(arr, index))
