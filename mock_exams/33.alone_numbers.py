'''
Alone Numbers
We will give you array and a target! You need to find all "alone"
elements in the array that match the given target. These elements are
alone if they have values before and after them, but those values are different from them.

Return new version of the given array where every element that matches the target
and is alone is replaced by whichever value to its left or right is larger.
'''

nums = [int(n) for n in input().split(', ')]
target = int(input())

for i in range(1, len(nums) - 1):
    if target == nums[i] and nums[i - 1] != target and nums[i + 1] != target:
        if nums[i - 1] > nums[i + 1]:
            nums[i] = nums[i - 1]
        else:
            nums[i] = nums[i + 1]
print(nums)
