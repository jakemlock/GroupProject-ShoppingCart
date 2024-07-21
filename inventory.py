import random


class Inventory:
    def __init__(self):
        # initializes the shop inventory (inventory is hard coded in with randomized stock count for each item and
        # randomized stock price for each item)
        self.ansi = {'cyan': '\u001b[36m', 'underline': '\033[4m', 'bold': '\033[1m', 'end': '\033[0m', }
        self.titles = ['Jaws', 'Poltergeist', 'Friday the 13th', 'Nightmare on Elm St.']
        self.costs = [10, 12, 15]
        self.inventory = {
            i: {'cost': self.costs[random.randint(0, len(self.costs) - 1)], 'stock': random.randint(1, 10)} for i in
            self.titles}

    # accessor methods
    def get_item(self, _item):
        """
        an accessor method for accessing an item in the inventory's cost and amount in stock
        :param self: the shop inventory object
        :param _item: an item passed by the user
        :return: if the item passed in is the inventory returns the item's cost and amount in stock
                if item is not in the inventory object the function displays a message notifying the user
        """
        if _item in self.inventory:
            return self.inventory[_item]
        elif _item not in self.inventory:
            print(f'{_item} not in inventory')

    def get_inventory(self):
        """
        an accessor method for displaying the contents of the inventory object
        :param self: the shop inventory object
        :return: nothing
        """
        # prints current store inventory
        print(f"{self.ansi['bold']}{self.ansi['cyan']}Our Current Inventory{self.ansi['end']}")
        print(self.ansi['underline'] + '{:25s} {:10s} {:5s}'.format('Item', 'Available', 'Cost') + self.ansi['end'])
        for k, v in self.inventory.items():
            print('{:25s} {:10d} {:5d}'.format(k, v['stock'], v['cost']))

    #mutator methods
    def checkout(self, items: dict):
        """
        a mutator method Cart checkout calls this method to reduce store's inventory
        this method alters the current inventory stock by decrementing the stock of an item in inventory, using the
        user's cart object items as the keys to decrement the values of the inventory objects stock aligned with those
        keys
        :param self: the shop inventory object
        :param items: passed in dictionary of a shopping cart object used for decrementing the shops inventory by the
                      amount of the item in their cart
        :return:
        """
        for i in items:
            self.inventory[i]['stock'] = self.inventory[i]['stock'] - items[i]
