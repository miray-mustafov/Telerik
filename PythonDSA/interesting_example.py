from datetime import datetime

"""
Time complexity of cubic function here?
At first, it looks like cubic() has O(n^3) but both functions practically scale quadratically,
considering the cases below.
"""


def fake_cubic(n):  # O(?)
    count = 0
    for a in range(n):
        for b in range(n):
            if a == b:
                for c in range(n):
                    count += 1
    return count


def linear(n):  # O(n)
    count = 0
    for a in range(n):
        count += 1
    return count


def quadratic(n):  # O(n^2)
    count = 0
    for a in range(n):
        for b in range(n):
            count += 1
    return count


def quadratic_2(n):  # O(n^2) but effective work complexity is O(n)
    count = 0
    for a in range(n):
        for b in range(n):
            if a == b:
                count += 1
    return count


n = 2
print(linear(n))
print(quadratic(n))
print(quadratic_2(n))

# n = 5000
# print()
# t1 = datetime.now()
# res1 = linear(n)
# t2 = datetime.now()
# res2 = quadratic(n)
# t3 = datetime.now()
# res3 = quadratic_2(n)
# t4 = datetime.now()
# print(res1, t2 - t1)
# print(res2, t3 - t2)
# print(res3, t4 - t3)
#
# print()
# t1 = datetime.now()
# res1 = quadratic(5000)
# t2 = datetime.now()
# res2 = fake_cubic(5000)
# t3 = datetime.now()
# print(res1,t2-t1)
# print(res2,t3-t2)

# quadratic(2983)  # 8898289
# fake_cubic(2983)  # 8898289
