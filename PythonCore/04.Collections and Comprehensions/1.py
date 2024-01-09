"""1. Write a list comprehension that filters
all the numbers which are less than 5 or larger than 15."""

# [1,15,2,8,31,5,9] -> [1,2,31]
arr = [1, 15, 2, 8, 31, 5, 9]
res_arr = [x for x in arr if x < 5 or x > 15]
print(res_arr)

"""2. Write a list comprehension that filters all the numbers which are prime.
You will need an is_prime function to use in the conditional part"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


res_arr2 = [x for x in arr if is_prime(x)]
print(res_arr2)
'''3. Write a list comprehension that all the strings which are longer than 5 symbols.

['cat', 'dog', 'elephant', 'cucumber'] -> ['elephant', 'cucumber']
'''
animals = ['cat', 'dog', 'elephant', 'cucumber']
res_animals = [x for x in animals if len(x) > 5]
print(res_animals)

'''4.
Write a list comprehension that filters all the users that have 
strong passwords. A 'strong' password means one lowercase, one uppercase, 
one digit and at least 8 symbols long.
Expected result: [('gosho', 'passwOrd1')]
'''
usr_passwords = [
    ('pesho', 'qwe345!'),
    ('gosho', 'passwOrd1'),
    ('penka', '1a2b3c4d'),
]

res_usr_passwords = [(usr, passw) for usr, passw in usr_passwords if (
        len(passw) >= 8 and
        any(ch.islower() for ch in passw) and
        any(ch.isupper() for ch in passw) and
        any(ch.isdigit() for ch in passw)
)]
print(res_usr_passwords)
