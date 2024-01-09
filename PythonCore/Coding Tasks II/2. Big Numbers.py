from itertools import zip_longest

n1, n2 = map(int, input().split())
list1 = map(int, input().split())
list2 = map(int, input().split())

res, carry = [], 0
for d1, d2 in zip_longest(list1, list2, fillvalue=0):
    sumed_digit = d1 + d2 + carry
    if sumed_digit > 9:
        res.append(sumed_digit % 10)
        carry = 1
    else:
        res.append(sumed_digit)
        carry = 0

if carry:  # !!!
    res.append(carry)

print(*res)

# n1, n2 = map(int, input().split())
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
# res, carry = [], 0
#
# i = 0
# while i < min(n1, n2):
#     summed_digit = list1[i] + list2[i] + carry
#     if summed_digit > 9:
#         res.append(summed_digit % 10)
#         carry = 1
#     else:
#         res.append(summed_digit)
#         carry = 0
#     i += 1
#
# biglist = list1 if n1 > n2 else list2
#
# while i < len(biglist):
#     summed_digit = biglist[i] + carry
#     if summed_digit > 9:
#         res.append(summed_digit % 10)
#         carry = 1
#     else:
#         res.append(summed_digit)
#         carry = 0
#     i += 1
#
# print(*res)
