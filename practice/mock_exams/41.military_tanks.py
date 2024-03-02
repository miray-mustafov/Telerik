'''
Military Tanks
Military scientists are training battle tanks using 
artificial intelligence. The first lesson is to teach 
them to move across the (x,y) - plane. They give them a sequence 
of moves and observe whether the tanks get to the correct (x, y) position 
on the field. This sequence is represented by string_list, and the character
at position i represents the tank's i-th move.
'''

# commands = input()
commands = 'LLRD'
x, y = 0, 0
for comm in commands:
    if comm == 'L':
        x -= 1
    elif comm == 'R':
        x += 1
    elif comm == 'U':
        y += 1
    elif comm == 'D':
        y -= 1
print(f"({x}, {y})")
