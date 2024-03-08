def array_contains_value_times_10(arr, index):
    if index >= len(arr) - 1:
        return 'false'

    if arr[index] * 10 == arr[index + 1]:
        return 'true'

    return array_contains_value_times_10(arr, index + 1)


arr = list(map(int, input().split(',')))
index = int(input())
print(array_contains_value_times_10(arr, index))
