def solution():
    text = input()
    if len(text) == 1: return text
    l = max_l = 0
    r = max_r = 1

    while r < len(text):
        if text[l] != text[r]:
            if r - l > max_r - max_l:
                max_l, max_r = l, r
            l = r
        r += 1

    if r - l > max_r - max_l:
        max_l, max_r = l, r

    return text[max_l: max_r]


print(solution())

''' examples
aCCCdddd => dddd
aCCCddd => CCC
abbCCCcddBBBxx => CCC
'''
