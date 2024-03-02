# def f(arr, index):
#     if index >= len(arr):
#         return False
#     if arr[index] == '6':
#         return True
#     return f(arr, index + 1)
#
#
# arr = input().split(',')
# index = int(input())
# print(f(arr, index))


def array_contains_6(arr, index):
    if index >= len(arr):
        return False
    if arr[index] == 6:
        return True
    return array_contains_6(arr, index + 1)


arr = input()
index = int(input())
print(array_contains_6(arr, index))
