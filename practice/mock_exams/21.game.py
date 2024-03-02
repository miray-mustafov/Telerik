# string_list = '501'
# sum = 0
# multiplication = 1
# counter = 0
# for i in range(3):
#     if int(string_list[i]) > 1:
#         multiplication *= int(string_list[i])
#     else:
#         sum += int(string_list[i])
#         counter +=1
# if sum == 3:
#     print(3)
# if counter == 2:
#     print(sum + multiplication)


n = 185
digit1 = int(n // 100)
digit2 = int((n // 10) % 10)
digit3 = int(n % 10)

case1 = digit1 + digit2 + digit3
case2 = digit1 * digit2 * digit3
case3 = digit1 * digit2 + digit3
case4 = digit1 + digit2 * digit3
case5 = digit1 * digit2 + digit3
case6 = digit1 + digit2 * digit3

max_result = max(case1, case2, case3, case4, case5, case6)
print(max_result)
