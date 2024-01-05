dictionary = []


def add_word(word, meaning):
    dictionary.append([word, meaning])


def update_meaning(word, meaning):
    for pair in dictionary:
        if pair[0] == word:
            pair[1] = meaning


def find_word(word):
    for pair in dictionary:
        if pair[0] == word:
            return pair
