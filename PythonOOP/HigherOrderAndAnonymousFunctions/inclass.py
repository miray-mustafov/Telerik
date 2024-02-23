from functools import reduce


# Filter Tasks
def less_than_5_or_greater_than_15(numbers):
    return list(filter(lambda n: n < 5 or n > 15, numbers))


def between_5_and_15(numbers):
    return list(filter(lambda n: 5 < n < 15, numbers))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_primes(numbers):
    return list(filter(is_prime, numbers))


def longer_than_5(strings):
    return list(filter(lambda s: len(s) > 5, strings))


def includes_substring(strings, substr):
    return list(filter(lambda s: substr in s, strings))


# Map Tasks
def double_numbers(numbers):
    return list(map(lambda n: n * 2, numbers))


def uppercase_strings(strings):
    return list(map(lambda s: s.upper(), strings))


def opposite_case_strings(strings):
    return list(map(lambda s: s.swapcase(), strings))


def normalize_strings(strings):
    return list(map(lambda s: s.capitalize(), strings))


# Reduce Tasks
def product_of_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)


def maximum_number(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)


def longest_string(strings):
    return reduce(lambda x, y: x if len(x) > len(y) else y, strings)


def reverse_string(string):
    return reduce(lambda x, y: y + x, string)


# Test cases
numbers = [1, 15, 2, 8, 31, 5, 9]
strings = ['cat', 'dog', 'elephant', 'cucumber']

print(less_than_5_or_greater_than_15(numbers))
print(between_5_and_15(numbers))
print(filter_primes(numbers))
print(longer_than_5(strings))
print(includes_substring(strings, 'uc'))
print()
print(double_numbers(numbers))
print(uppercase_strings(strings))
print(opposite_case_strings(strings))
print(normalize_strings(strings))
print()
print(product_of_numbers([1, 2, 3, 4, 5]))
print(maximum_number([7, 13, 72, 14]))
print(longest_string(strings))
print(reverse_string("apple"))
