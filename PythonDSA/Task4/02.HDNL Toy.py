def generate_tags(lines):
    tags = []
    for line in lines:
        level = int(line[1:])
        while tags and tags[-1][1] >= level:
            print(' ' * tags[-1][1] + '</' + tags.pop()[0] + '>')
        print(' ' * level + '<' + line + '>')
        tags.append((line, level))

    while tags:
        print(' ' * tags[-1][1] + '</' + tags.pop()[0] + '>')


N = int(input())
lines = [input() for _ in range(N)]
generate_tags(lines)
