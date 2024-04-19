import commands.category as categories
import commands.users as users
import commands.orders as orders
import commands.products as products
from storage import TokenStorage


def welcome_prompt():
    token = TokenStorage.get_token()
    if not token:
        print('Hello, please [L]ogin or [R]egister')
        choice = input().upper()
        if choice == 'L':
            users.login()
        elif choice == 'R':
            users.register()
        else:
            welcome_prompt()  # you must log in!
    else:
        print('Hello, ', end='')
        users.info(token)


def main():
    welcome_prompt()
    while True:
        print('\nCommands = [C]ategories / [P]roducts / [U]sers / [O]rders / [EXIT]')
        choice = input().upper()

        if choice == 'C':
            categories.select_action()
        elif choice == 'P':
            products.select_action()
        elif choice == 'U':
            users.select_action()
        elif choice == 'O':
            orders.select_action()
        elif choice == 'EXIT':
            print("\nClient Stopped")
            break
        else:
            print("No such command")


if __name__ == '__main__':
    main()
