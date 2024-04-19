import commands.category as categories
import commands.user as users
import commands.product as products
import commands.order as orders


def main():
    print('Commands = categories / products / users / orders')
    cmd = input()

    if cmd == 'categories':
        categories.select_action()
    if cmd == 'products':
        users.select_action()
    if cmd == 'users':
        products.select_action()
    if cmd == 'orders':
        products.select_action()


if __name__ == '__main__':
    main()
