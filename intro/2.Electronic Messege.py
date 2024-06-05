s = input()

import re

broken_pattern = r'[^a-zA-Z0-9\s]'
longest_seq_br_chars = current_seq_br_chars = 0
for char in s:
    if char == '.':
        break
    if re.match(broken_pattern, char):
        current_seq_br_chars += 1
    else:
        longest_seq_br_chars = max(longest_seq_br_chars, current_seq_br_chars)
        current_seq_br_chars = 0

print(longest_seq_br_chars)
