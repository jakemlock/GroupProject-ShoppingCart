from inventory import Inventory
class Cart:

    def __init__(self):
        # initialize the user's shopping cart
        self.shopping_cart = {}
        self.store_inventory = Inventory()

    # accessor methods
    def get_cart(self):
        # get cart contents
        if not self.shopping_cart:
            print("Your cart is empty.")
        else:
            print("Your cart includes: ")
            for item, quantity in self.shopping_cart.items():
                print(item + ": " + str(quantity))
        return self.shopping_cart
        pass

    # mutator methods
    def add_cart(self):
        # add item to cart
        item = input('Which item would you like to add? ')
        item_info = self.store_inventory.get_item(item)
        if item_info:
            quantity = int(input('How many would you like to add? '))
            if item_info['stock'] >= quantity:
                if item in self.shopping_cart:
                    self.shopping_cart[item] += quantity
                else:
                    self.shopping_cart[item] = quantity
                print("Added " + str(quantity) + " of " + item + " to your cart.")
            else:
                print("Sorry, we only have " + str(item_info['stock']) + " of " + item + " in stock.")
                self.add_cart()
        pass

    def remove_cart(self, item):
        # remove item from cart
        try:
            self.shopping_cart.pop(item)
            print(f"{item} removed! ")
        except:
            print(f"{item} not in your cart! ")


    def edit_cart(self, item):
        if item in self.shopping_cart:
            quantity = int(input('How many would you like to remove from your cart? '))
            if self.shopping_cart[item] >= quantity:
                self.shopping_cart[item] -= quantity
                if self.shopping_cart[item] <= 0:
                    del self.shopping_cart[item]
                print("Removed " + str(quantity) + " of " + item + " from your cart.")
            else:
                print("You only have " + str(self.shopping_cart[item]) + " of " + item + " in your cart.")
                self.edit_cart(item)
        else:
            print(item + " is not in your cart.")
        pass

    def checkout(self):
        # list total, remove stock from store's inventory and reset cart
        total = 0
        for item, quantity in self.shopping_cart.items():
            item_info = self.store_inventory.get_item(item)
            if item_info:
                total += item_info['cost'] * quantity
                self.store_inventory.checkout({item: quantity})
        print("Your total is $" + str(total) + ". Thank you for shopping with us!")
        self.shopping_cart.clear()
        pass