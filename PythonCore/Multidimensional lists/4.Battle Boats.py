def read_player_board(rows):
    player = []

    for _ in range(rows):
        player.append(input().split())

    return player


def read_coordinates():
    commands = []

    cmd = input()

    while cmd != 'END':
        r, c = map(int, cmd.split()[1:])  # skip the pointless 'Shoot'

        commands.append([r, c])

        cmd = input()

    return commands


def shoot_at(player, r, c):
    if player[r][c] == '0':

        player[r][c] = 'x'

        return 'Missed'

    elif player[r][c] == '1':

        player[r][c] = 'x'

        return 'Booom'

    else:

        return 'You already shot there!'


def count_surviving(player):
    total = 0

    for row in player:
        total += row.count('1')

    return total


rows, cols = map(int, input().split())

player_1 = read_player_board(rows)

player_2 = read_player_board(rows)

coordinates = read_coordinates()

player_1_turn = True

for r, c in coordinates:

    if player_1_turn:

        r, c = -r - 1, -c - 1  # Player two coords are reversed for no reason

        print(shoot_at(player_2, r, c))

    else:

        print(shoot_at(player_1, r, c))

    player_1_turn = not player_1_turn

print(f'{count_surviving(player_1)}:{count_surviving(player_2)}')
'''
input:
2 2

0 1

1 1

1 0

1 1

Shoot 1 1

Shoot 0 1

Shoot 0 0

Shoot 0 0

Shoot 1 1

Shoot 1 0

END

output:
Booom

Booom

Booom

Missed

You already shot there!

Booom

1:1
'''
