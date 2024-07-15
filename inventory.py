class Inventory:
    def __init__(self):
        # initialize the store's inventory
        self.inventory = {'book': {'stock': 4, 'cost': 10.00}, 'pencil': {'stock': 3, 'cost': 4.00}}

    # accessor methods
    def get_item(self, _item):
        # list store's available inventory
        if _item in self.inventory:
            return self.inventory[_item]
        elif _item not in self.inventory:
            print('Item not in inventory')

    def get_inventory(self):
        print('Our Current Inventory\n_______________________')
        print(f'Item\tAvailable\tCost')
        for k, v in self.inventory.items():
            print(f"{k}\t{v['stock']}\t\t{v['cost']}")

