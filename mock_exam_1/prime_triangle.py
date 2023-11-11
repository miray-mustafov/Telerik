'''
Prime Triangle
Description
We know that you love math, so we have prepared a very interesting task, that involves both geometry and prime numbers.

By a given N number, from which you need to generate a sequence of 1 to N inclusive. For every prime number in that sequence, you need to print out all the other numbers before it (and the number itself), whether they are prime or not

Note:
For the purposes of this task (and against the laws of mathematics), the number 1 is considered as prime.

Let's make things simpler:
Print 0 if the numbers is not prime
Print 1 if the number is prime

Input
Read from the standard input
On the single line, find the number N
The input data will always be valid and in the format described. There is no need to check it explicitly
Output
Print on the standard output
The output should consist of several lines of digits each of which can be either 1 or 0
Without any space between them
Sample tests
Input
10
Output
1
11
111
11101
1110101
'''


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


n = 27
line, zeroes = '1', ''
print(line)
for d in range(2, n+1):
    if is_prime(d):
        line += zeroes + '1'
        zeroes = ''
        print(line)
    else:
        zeroes += '0'
