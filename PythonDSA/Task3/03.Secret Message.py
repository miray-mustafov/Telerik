def decode_message(s):
    def recursion(s):
        if not s or s == '}':
            return ''

        prefix, i = '', 0
        while i < len(s) and s[i].isalpha():  # form current prefix if present
            prefix, i = prefix + s[i], i + 1
        if i == len(s) or s[i] == '}':
            return prefix + recursion(s[i + 1:])

        num = 0
        while not s[i] == '{':  # form the number
            num, i = num * 10 + int(s[i]), i + 1

        txt, i = '', i + 1
        while s[i].isalpha():  # form the in brackets txt msg
            txt, i = txt + s[i], i + 1

        res = prefix
        if s[i].isdigit():
            for t in range(num):
                res += txt + recursion(s[i:])
        elif s[i] == '}':
            res += num * txt + recursion(s[i + 1:])
        return res

    suffix = ''
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '}':
            break
        suffix = s[i] + suffix
    a = s[:i + 1]
    res = recursion(s[:i + 1]) + suffix
    return res


# s = input()
# print(decode_message(s))

s = '4{a}2{xz}'
decoded_s = decode_message(s)
print(decoded_s, decoded_s == 'aaaaxzxz')

s2 = 'а3{z2{xy}oo}аzb'  # Test this one
decoded_s2 = decode_message(s2)
print(decoded_s2, decoded_s2 == 'аzxyxyoozxyxyoozxyxyooаzb')

s3 = 'a3{cd2{a}f}ef'
decoded_s3 = decode_message(s3)
print(decoded_s3, decoded_s3 == 'acdaafcdaafcdaafef')
