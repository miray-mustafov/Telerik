import console_dictionary


def execute_instruction(line):
    line = line.split(':')
    if len(line) == 2:
        action, word = line
    else:
        action, word, meaning = line

    if action == 'add':
        console_dictionary.add_word(word, meaning)
        return 'Added word'
    elif action == 'update':
        console_dictionary.update_meaning(word, meaning)
        return 'Meaning updated'
    elif action == 'find':
        found = console_dictionary.find_word(word)
        return f'{found[0]}: "{found[1]}"' if found else 'No such word'
