def F(string_list):
    if not string_list:
        return 0
    ch = string_list.pop()
    if ch == 'x':
        return 1 + F(string_list)
    return 0 + F(string_list)


string = input()
string_list = [ch for ch in string]
print(F(string_list))
