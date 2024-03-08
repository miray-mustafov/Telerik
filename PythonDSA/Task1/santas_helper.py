"""
Santa's Helper
It's very busy over at the North Pole nowadays. Today kids are smarter and want more expensive gifts. It was easy for Santa when everything a kid would wish for was a new book or a new bike (eventually they got socks and sweaters, but that's a different topic). Now, on the other hand, children want VR headsets, electric scooters, and drones. What is more, kids used to get one wish only, and now they have whole lists of wishes!

Help Santa by writing a program that makes keeping up with kids wishes a little easier. Each wish has the name of the item, how much it would cost the dwarfs to make it and the name of the child that requested it. Design a system that executes N commands, given in the input (a single command at a line):

AddWish item_name;estimated_price;child_name - adds a new wish to Santa's list by given name of the item, estimated price and the name of the child. If a wish with the same name / price / child name already exists, the newly added wish does not affect existing ones (duplicates are allowed). As a result, the command prints "Wish added".
DeleteWishes child_name - You have to be on the "Good kids list" in order to get your present. If someone is not, Santa needs to be able to delete all wishes by that kid. As a result, the command prints "X Wishes deleted" where X is the number of deleted wishes or "No Wishes found" if no such wish exist.
FindWishesByPriceRange fromPrice;toPrice – Santa needs to balance the books from time to time, so there needs to be a command that finds all wishes whose estimated price is greater or equal than fromPrice and less or equal than toPrice. As a result the command prints a list of wishes in the format {item_name;child_name;estimated_price}. The items should be ordered in alphabetical order. You should print each order on a single line. If no orders exist within the specified price range, the command prints “No Wishes found”.
FindWishesByChild child_name – finds all wishes by given child name. As a result the command prints a list of wishes in format {item_name;child_name;estimated_price}. The list items should be ordered in alphabetical order. You should print each wish on a single line. If no wishes exist by the specified child, the command prints “No Wishes found”.
See the examples bellow.

Input
The input data is read from the standard input (the console).

On the first line you will receive the number N of the commands.
On the next N lines you will be given a command in the format described above.
Output
The output data is printed on the standard output (the console).

The output should contain the output from each command from the input.
Constraints
N will be between 1 and 60000
All names and other strings consist of alphabetical characters, numbers and spaces.
Prices are given as real numbers with up to 2 digits after the decimal point, (e.g. 35.18, or 120).
The ‘.’ symbol is used as decimal separator.
Prices should be printed with exactly 2 digits after the decimal point (e.g. 120.30 instead of 120.3).
Sample Tests
Input
10
AddWish Electric Scooter 2000Z;1536.50;Stefan
AddWish Fortnite Skin;3000;Stefan
AddWish AMD Radeon;4099.99;Pesho
AddWish Apple AirPods;200000;Kiril
AddWish Socks;10000;Tosho
AddWish Swater;999;Stefan
FindWishesByChild Stefan
DeleteWishes Stefan
FindWishesByChild Stefan
FindWishesByPriceRange 100000;200000
Output
Wish added
Wish added
Wish added
Wish added
Wish added
Wish added
{Electric Scooter 2000Z;Stefan;1536.50}
{Fortnite Skin;Stefan;3000.00}
{Swater;Stefan;999.00}
3 Wishes deleted
No Wishes found
{Apple AirPods;Kiril;200000.00}
Input
8
AddWish Electric Scooter 2000Z;3500.05;Rayko Petrov
AddWish Fortnite Skin;3000;Rayko Petrov
AddWish AMD Radeon;16400;Hristo
AddWish Apple AirPods;21111.50;Nadya
FindWishesByChild Toshko
DeleteWishes Rayko Petrov
FindWishesByChild Rayko Petrov
FindWishesByPriceRange 5000;30000
Output
Wish added
Wish added
Wish added
Wish added
No Wishes found
2 Wishes deleted
No Wishes found
{AMD Radeon;Hristo;16400.00}
{Apple AirPods;Nadya;21111.50}
"""

class Wish:
    def __init__(self, item, price: float, name):
        self.item = item
        self.price = price
        self.name = name

    def __str__(self):
        return f'{{{self.item};{self.name};{self.price:.2f}}}'


class SantaHelper:
    def __init__(self):
        self.wishes_by_name = {}

    def add_wish(self, item_name, estimated_price, child_name):
        estimated_price = float(estimated_price)
        wish = Wish(item_name, estimated_price, child_name)
        if child_name not in self.wishes_by_name:
            self.wishes_by_name[child_name] = []
        self.wishes_by_name[child_name].append(wish)
        print('Wish added')

    def delete_wishes(self, child_name):
        if child_name not in self.wishes_by_name:
            print('No Wishes found')
            return
        x = len(self.wishes_by_name[child_name])
        del self.wishes_by_name[child_name]

        print(f'{x} Wishes deleted')

    def find_wishes_by_price_range(self, fromPrice, toPrice):
        wishes = []
        fromPrice = float(fromPrice)
        toPrice = float(toPrice)
        for _, child_wishes in self.wishes_by_name.items():
            for wish in child_wishes:
                if fromPrice <= wish.price <= toPrice:
                    wishes.append(wish)
        if not wishes:
            print("No Wishes found")
            return
        for wish in sorted(wishes, key=lambda w: w.item):
            print(str(wish))

    def find_wishes_by_child(self, child_name):
        if child_name not in self.wishes_by_name:
            print('No Wishes found')
            return
        wishes = self.wishes_by_name[child_name]
        for wish in sorted(wishes, key=lambda w: w.item):
            print(str(wish))

    COMMANDS = {
        'AddWish': add_wish,
        'DeleteWishes': delete_wishes,
        'FindWishesByPriceRange': find_wishes_by_price_range,
        'FindWishesByChild': find_wishes_by_child,
    }


n = int(input())
santa_system = SantaHelper()
for _ in range(n):
    command, params = input().split(" ", 1)
    params = params.split(';')
    SantaHelper.COMMANDS[command](santa_system, *params)
"""
10
AddWish Electric Scooter 2000Z;1536.50;Stefan
AddWish Fortnite Skin;3000;Stefan
AddWish AMD Radeon;4099.99;Pesho
AddWish Apple AirPods;200000;Kiril
AddWish Socks;10000;Tosho
AddWish Swater;999;Stefan
FindWishesByChild Stefan
DeleteWishes Stefan
FindWishesByChild Stefan
FindWishesByPriceRange 100000;200000
"""
