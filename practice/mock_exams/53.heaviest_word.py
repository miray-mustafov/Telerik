'''
Heaviest Word
The Academy needs you! We have this list of words and we have to find the heaviest one, but we haven't a clue how to
approach the problem.

Word heaviness is determined by summing all the letters in it. The letter value corresponds to the position in the
English alphabet - where a is 1 and z is 26. For example, the word alpha has a weight of 1 + 12 + 16 + 8 + 1 = 38.
Treat lower- and uppercase letters the same, so a and A both have the value 1.

Your task is to create a program that finds the heaviest word and prints its weight and the word itself to the
standart output.

Input
On the first line, N - the number of words to follow.
On the next N lines - a single word.
Output
The heaviest weight and the heaviest word, separated by a space.
'''

alphabet_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
                 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                 'k': 11, 'l': 12, 'm': 13, 'num': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
                 }
n = int(input())
heaviest_weight, heaviest_word = 0, ''
for _ in range(n):
    current_word = input()
    current_weight = sum([alphabet_dict[ch] for ch in current_word if ch.isalpha()])
    if current_weight > heaviest_weight:
        heaviest_weight = current_weight
        heaviest_word = current_word
print(heaviest_weight, heaviest_word)
