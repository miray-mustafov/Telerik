nums, n, is_true = input().split(','), int(input()), True
for i in range(n):
    if nums[i] != nums[-1 - i]:
        is_true = False
        break

if is_true:
    print(f'true {",".join(nums[:n])}')
else:
    print(f'false {nums[i]},{nums[-1 - i]}')  # n > 0, n < nums.length
