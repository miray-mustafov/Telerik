def f(base, n):
    if n == 0:
        return 1
    elif n == 1:
        return base
    elif n % 2 == 0:
        half_power = f(base, n // 2)
        return half_power * half_power
    else:
        half_power = f(base, (n - 1) // 2)
        return base * half_power * half_power


base = int(input())
n = int(input())
result = f(base, n)
print(result)

# base = int(input())
# string = int(input())
#
#
# def solution(base, string):
#     if string == 1:
#         return base
#     elif string == 0:
#         return 1
#     return base * solution(base, string - 1)
#
#
# print(solution(base, string))
