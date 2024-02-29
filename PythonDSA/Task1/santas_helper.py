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
