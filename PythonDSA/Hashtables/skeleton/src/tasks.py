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
    catalogue_set = set(catalogue)
    res = 0
    for c in coins:
        if c in catalogue_set:
            res += 1
    return res


coins = 'aaAb'
catalogue = 'ab'
print(special_coins(coins, catalogue))


def are_isomorphic(s1: str, s2: str) -> bool:
    d = {}
    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]] = s2[i]
        elif d[s1[i]] != s2[i]:
            return False
    return True


print(are_isomorphic('tidal', 'paper'))
# 'tidal'
# 'paper'
