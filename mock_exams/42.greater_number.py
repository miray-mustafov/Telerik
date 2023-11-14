'''
Greater Number
You are given two arrays where the elements of the first one are subset of the elements of the second one. For each element
in the first array, find the next greater element in the second array, starting at the position of the given element.
'''

arr1 = [int(n) for n in input().split(',')]
arr2 = [int(n) for n in input().split(',')]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            found_bigger = False
            for k in range(j, len(arr2)):
                if arr2[k] > arr1[i]:
                    arr1[i] = arr2[k]
                    found_bigger = True
                    break
            if not found_bigger:
                arr1[i] = -1
            break

print(','.join([str(num) for num in arr1]))
