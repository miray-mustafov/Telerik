anagrams = input().split()
unique_anagrams = set()
res = []
for word in anagrams:
    word_tuple = tuple(sorted(word))
    if word_tuple not in unique_anagrams:
        res.append(word)
    unique_anagrams.add(word_tuple)

print(*res)
# print(tuple(sorted('ear')))
# print(sorted('rea'))
