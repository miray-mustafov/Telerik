def get_word():
    word = input('Give only letter word! length >= 3: ')
    if len(word) < 3:
        return get_word()
    for i in range(len(word)):  # check each element in word if is alphabet letter
        if not word[i].isalpha():
            return get_word()
    return word.lower()


def get_initial_positions(l):
    positions = [False] * l
    positions[0] = positions[-1] = True
    return positions


def hide_word(word, positions):
    res = ''
    for i in range(len(word)):
        if positions[i] == True:
            res += word[i]
        else:
            res += '-'
    return res


def check_guess(word, letter, positions):
    for i in range(1, len(word) - 1):
        if letter == word[i]:
            positions[i] = True
    return positions


def check_for_win(positions):
    if all(positions):
        return True
    return False


def play_hangman():
    word = get_word()
    lives = int(input('Choose lives count: '))
    positions = get_initial_positions(len(word))
    # hidden = hide_word(word, positions)

    while True:  # we will check for win or loss in the loop and break accordingly
        print()
        print(hide_word(word, positions))
        next_letter = input('Try to guess with a letter: ')
        new_positions = check_guess(word, next_letter, positions.copy())

        # Option 1 - both lists are the same - the next_letter is not a correct guess
        if new_positions == positions:
            print('No such letter or already guessed')
            lives = lives - 1
            print(f'Lives remaining: {lives}')

            if lives == 0:  # no more lives - break
                print('You lose!')
                break

        # Option 2 - if the lists are not the  same, all values in new_positions may be True
        #    we use the check_for_win function to validate
        elif check_for_win(new_positions):
            print('You win!')
            break

        # Option 3 - the two lists are not the same, and new_postions is not all True - this means that another letter is guessed. We need to print it.
        else:
            print('Another letter guessed!')
            print(hide_word(word, new_positions))

            # it's important to update the positions list for the next iteration
            positions = new_positions


play_hangman()
