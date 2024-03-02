"""
Hi,
What do you think about the time complexity of second function here?
At first, it looks like cubic() has O(string^3) but both functions practically scale quadratically,
considering the cases below.
GPT is confused and gives both answers sometimes.
"""


def quadratic(n):  # O(string^2)
    count = 0
    for a in range(n):
        for b in range(n):
            count += 1
    print(count)


def cubic(n):  # O(?)
    count = 0
    for a in range(n):
        for b in range(n):
            if a == b:
                for c in range(n):
                    count += 1
    print(count)


cubic(20)  # 400 (20*20)
cubic(30)  # 900 (30*30)
print()
quadratic(20)  # 400 (20*20)
quadratic(30)  # 900 (30*30)
