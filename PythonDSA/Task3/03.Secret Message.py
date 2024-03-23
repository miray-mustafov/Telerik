def decode_message(s):
    def recursion(s, i):
        decoded_text = ''
        while i < len(s) and s[i] != '}':
            if s[i].isdigit():
                num_start = i
                while s[i].isdigit():
                    i += 1
                repetitions = int(s[num_start:i])
                i += 1  # Move past the '{'
                inner_text, i = recursion(s, i)
                decoded_text += inner_text * repetitions
            else:
                decoded_text += s[i]
                i += 1
        return decoded_text, i + 1  # Move past the '}'

    decoded_text, _ = recursion(s, 0)
    return decoded_text

# Test cases
s1 = '4{a}2{xz}'
decoded_s1 = decode_message(s1)
print(decoded_s1 == 'aaaaxzxz')

s2 = 'аzb3{za2{xy}oo}аzb'
decoded_s2 = decode_message(s2)
print(decoded_s2 == 'аzxyxyoozxyxyoozxyxyooаzb')

s3 = 'a3{cd2{a}f}ef'
decoded_s3 = decode_message(s3)
print(decoded_s3 == 'acdaafcdaafcdaafef')