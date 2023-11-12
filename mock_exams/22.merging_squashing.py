n = int(input())
nums = [input() for _ in range(n)]
merged, squashed = [], []
for i in range(1, nums):
    a, b = int(nums[i-1][0]), int(nums[i-1][1])
    c, d = int(nums[i][0]), int(nums[i][1])
    merged.append(str(b)+str(c))
    squashed.append(a*(b+c)*d)

[print(num, end=' ') for num in merged]
[print(num, end=' ') for num in squashed]
