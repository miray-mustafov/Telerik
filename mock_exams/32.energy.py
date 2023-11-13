'''
Energy
Energy drink calculations are simple - in order to decide how many drinks you should have,
you are given a number. Find the sum of the even digits and the sum of the odd digits of that
number, then compare these sums and:

If the sum of the even digits is bigger, drink energy drinks.
If the sum of the odd digits is bigger, drink cups of coffee.
If the two sums are equal, drink both.
'''

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
