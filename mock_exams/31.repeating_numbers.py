'''
Repeating Numbers
Write a program that accepts an array of integers and returns
the one that occurs the most times. If there are two numbers that
occur the same amount of times, return the smaller of the two.
'''
n = int(input())
occurrences = {}
for _ in range(n):
    num = int(input())
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

max_rep_num, max_reps = occurrences.popitem()
for rep_num, reps in occurrences.items():
    if reps > max_reps:
        max_rep_num, max_reps = rep_num, reps
    elif reps == max_reps:
        max_rep_num = min(max_rep_num, rep_num)

print(max_rep_num)