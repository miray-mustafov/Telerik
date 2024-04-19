import commands.category as categories


def main():
    print('Commands = categories / products / users / orders')
    cmd = input()

    if cmd == 'categories':
        categories.select_action()
    if cmd == 'products':
        raise NotImplementedError()
    if cmd == 'users':
        raise NotImplementedError()
    if cmd == 'orders':
        raise NotImplementedError()


if __name__ == '__main__':
    main()
