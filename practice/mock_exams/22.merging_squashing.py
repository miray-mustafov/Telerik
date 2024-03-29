'''
Merging and Squashing
We have the following operations defined for two-digit numbers. There are two possible ways of merging them:

Merging ab and cd produces bc
42 merged with 17 produces 21
17 merged with 42 produces 74
Squashing ab and cd produces a(b+c)d - the middle digit is the sum of b and c
42 squashed with 17 produces 437
39 squashed with 57 produces 347 (9 + 5 = 14, we use only the 4)
You have a sequence of N two-digit numbers. Your task is to merge and squash each pair of adjacent numbers.

Input
All input data is read from the standard input

On the first line, you will receive an integer N
On the next N lines you will receive N two-digit numbers
Each number will be on a separate line
Output
The output data is printed on the standard output

On the first output line print the merged numbers

There should be N - 1 of them
Separate them by spaces
On the second output line print the squashed numbers

There should be N - 1 of them
Separate them by spaces
Constraints
2 <= N <= 1000
Numbers will consist of two non-zero digits
The input data will always be correct and there is no need to check it explicitly
Sample Tests
Input
4
12
23
34
45
Output
22 33 44
143 264 385
Input
5
11
22
11
22
11
Output
12 21 12 21
132 231 132 231
'''


# string = int(input())
# nums = [input() for _ in range(string)]

n = 4
nums = ['12', '23', '34', '45']
merged, squashed = [], []
for i in range(1, len(nums)):
    a, b = nums[i-1][0], nums[i-1][1]
    c, d = nums[i][0], nums[i][1]
    merged.append(b+c)
    squashed.append(a+(str((int(b)+int(c)) % 10))+d)

print(*merged, sep=' ')
print(*squashed, sep=' ')
