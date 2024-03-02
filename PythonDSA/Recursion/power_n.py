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
# string_list = int(input())
#
#
# def f(base, string_list):
#     if string_list == 1:
#         return base
#     elif string_list == 0:
#         return 1
#     return base * f(base, string_list - 1)
#
#
# print(f(base, string_list))
