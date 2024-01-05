"""
2. Write a function that 'merges' !!two equal length numbers!!. The merging operation adds the digits that are in the
same positions and if the result is greater than 9, only the last digit remains. So 1 + 2 = 3, but 8 + 5 = 3 also.
"""


def merge(a, b):
    a, b = str(a), str(b)
    res = 0
    for i in range(len(a)):
        current_digit = int(a[i]) + int(b[i])
        if current_digit > 9:
            current_digit %= 10
        res = res * 10 + current_digit
    return res


test = merge(123, 123)  # x = 246
test2 = merge(789, 123)  # x = 802 (7 + 1 = 8, 8 + 2 = 10, 9 + 3 = 12)
print(test)
print(test2)
