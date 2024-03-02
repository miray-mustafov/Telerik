def F(string):
    if len(string) < 2:
        return 0
    if string[-1] == 'i':
        if string[-2] == 'h':
            return 1 + F(string[:-2])
    return 0 + F(string[:-1])


string = input()
print(F(string))
