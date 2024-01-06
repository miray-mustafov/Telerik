i = int(input())
arr = list(map(int, input().split(',')))
i = i % len(arr)

command, forw, backw = input(), 0, 0
while command != 'exit':
    steps, direction, size = command.split()
    steps, size = int(steps), int(size)

    if direction == 'forward':
        for _ in range(steps):
            i = (i + size) % len(arr)
            forw += arr[i]
    elif direction == 'backwards':
        for _ in range(steps):
            i = (i - size) % len(arr)
            backw += arr[i]

    command = input()

print(f'Forward: {forw}\nBackwards: {backw}')
