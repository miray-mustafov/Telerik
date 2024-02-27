words = ['pesho', 'gosho', 'pesho']


def count_occurrences(words: list) -> dict:
    d = {}
    for w in words:
        if w not in d:
            d[w] = 0
        d[w] += 1
    return d


print(count_occurrences(words))


def two_sum(numbers: list, target_sum: int) -> tuple:
    d = {num: i for i, num in enumerate(numbers)}

    for i, num in enumerate(numbers[:-1]):
        reduction = target_sum - num
        if reduction in d and d[reduction] != i:
            return i, d[reduction]
    return -1, -1


numbers = [3, 0, 2, 4, 1]
target_sum = 7
print(two_sum(numbers, target_sum))


def special_coins(coins: str, catalogue: str) -> int:
    raise NotImplementedError()


def are_isomorphic(s1: str, s2: str) -> bool:
    raise NotImplementedError()
