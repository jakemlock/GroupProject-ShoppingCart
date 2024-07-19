import random


class Inventory:
    def __init__(self):
        # initialize the store's inventory
        self.ansi = {'cyan': '\u001b[36m', 'underline': '\033[4m', 'bold': '\033[1m', 'end': '\033[0m', }
        self.titles = ['Jaws', 'Poltergeist', 'Friday the 13th', 'Nightmare on Elm St.']
        self.costs = [10, 12, 15]
        self.inventory = {
            i: {'cost': self.costs[random.randint(0, len(self.costs) - 1)], 'stock': random.randint(1, 10)} for i in
            self.titles}

    def get_item(self, _item):
        #
        if _item in self.inventory:
            return self.inventory[_item]
        elif _item not in self.inventory:
            print(f'{_item} not in inventory')

    def get_inventory(self):
        # prints current store inventory
        print(f"{self.ansi['bold']}{self.ansi['cyan']}Our Current Inventory{self.ansi['end']}")
        print(self.ansi['underline'] + '{:25s} {:10s} {:5s}'.format('Item', 'Available', 'Cost') + self.ansi['end'])
        for k, v in self.inventory.items():
            print('{:25s} {:10d} {:5d}'.format(k, v['stock'], v['cost']))

    def checkout(self, items: dict):
        # Cart checkout calls this method to reduce store's inventory
        for i in items:
            self.inventory[i]['stock'] = self.inventory[i]['stock'] - items[i]
