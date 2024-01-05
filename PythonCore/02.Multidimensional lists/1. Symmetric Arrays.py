n = int(input())
for _ in range(n):
    is_symetric = 'Yes'
    arr = input().split()
    for i in range(len(arr) // 2):
        if not arr[i] == arr[len(arr) - 1 - i]:
            is_symetric = 'No'
            break
    print(is_symetric)
