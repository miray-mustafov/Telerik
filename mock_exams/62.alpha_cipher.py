cipher = ''
for _ in range(5):
    num = input()
    product_of_digits = int(num[0]) * int(num[1]) * int(num[2])
    product_of_digits = product_of_digits % 10
    cipher+=str(product_of_digits)
print(cipher)

