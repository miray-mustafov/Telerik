nums = input().split()
groups = [[], [], []]
for num in nums:
    groups[int(num) % 3].append(int(num))
for group in groups:
    print(*group, sep=' ')

''' Inputs
1 2 3 4 5 6 7
result
3 6
1 4 7
2 5

3 3 3 3 3
res
3 3 3 3 3
'''
