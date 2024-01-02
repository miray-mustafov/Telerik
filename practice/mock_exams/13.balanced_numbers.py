'''
Balanced Numbers
A balanced number is a 3-digit number whose second digit is equal to the sum of the first and last digit.

Write a program which reads and sums balanced numbers. You should stop when an unbalanced number is given.

Input
Input data is read from the standard input

Numbers will be given
Each one will be on a separate line
Output
Print to the standard output

Constraints
No more than 1000 numbers will be given
Sample tests
Input
132
123
Output
 132
Input
275
693
110
742
Output
1078
'''


def is_balanced(num):
    mid = (num % 100) // 10
    left = num // 100
    right = num % 10
    return mid == left + right


total_sum = 0

while True:
    try:
        num = int(input())

        if is_balanced(num):
            total_sum += num
        else:
            break
    except ValueError:
        break

print(total_sum)
