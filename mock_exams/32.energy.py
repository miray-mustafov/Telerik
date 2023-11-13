number = input()
even, odd = 0, 0
for digit in number:
    digit = int(digit)
    if digit % 2 == 0:
        even += digit
    else:
        odd += digit

if even > odd:
    print(f"{even} energy drinks")
elif odd > even:
    print(f"{odd} cups of coffee")
else:
    print(f"{odd} of both")
