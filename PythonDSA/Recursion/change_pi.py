pi = '3.14'


def F(string):
    if len(string) < 2:
        return string
    if string[-1] == 'i':
        if string[-2] == 'p':
            return F(string[:-2]) + pi
    return F(string[:-1]) + string[-1]


string = input()
print(F(string))
