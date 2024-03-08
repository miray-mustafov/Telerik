def f(message, current_decoding, cipher_dict, possibilities):
    if len(message) == 0:
        possibilities.append(current_decoding)
        return

    for num, letter in cipher_dict.items():
        if num and message.startswith(num):
            f(message[len(num):], current_decoding + letter, cipher_dict, possibilities)


message =  "1122"
cipher_sequence = 'A1B12C11D2'

cipher_dict, cur_letter, cur_num = {}, cipher_sequence[0], ''
for ch in cipher_sequence[1:]:
    if ch.isdigit():
        cur_num += ch
    else:
        cipher_dict[cur_num] = cur_letter
        cur_letter = ch
        cur_num = ''
cipher_dict[cur_num] = cur_letter

possibilities = []
f(message, "", cipher_dict, possibilities)
print(len(possibilities))
print("\n".join(m for m in sorted(possibilities)))