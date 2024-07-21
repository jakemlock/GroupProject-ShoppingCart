from inventory import Inventory


class Cart:

    def __init__(self):
        # initialize the user's shopping cart
        self.shopping_cart = {}
        self.store_inventory = Inventory()

    # accessor methods
    def get_cart(self):
        """
        an accessor method used to return the user's current shopping cart object containing the items they have chosen
        or returns a message if their cart is currently empty
        :return: if the cart is not empty, the function returns the user's current shopping cart object
        """
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
        """
        a mutator method used to add an item from the shop inventory and the amount the user selects to the user's
        cart object
        :return:
        """
        item = input('Which item would you like to add? ')
        item_info = self.store_inventory.get_item(item)
        if item_info:
            quantity = int(input('How many would you like to add? '))
            if item_info['stock'] >= quantity:
                if item in self.shopping_cart:
                    if self.shopping_cart[item] < item_info['stock']:
                        self.shopping_cart[item] += quantity
                        print("Added " + str(quantity) + " of " + item + " to your cart.")
                    else:
                        print(
                            f"Sorry, we only have {item_info['stock']} of {item} in stock. Your cart currently has {self.shopping_cart[item]} of {item}")
                else:
                    self.shopping_cart[item] = quantity
                    print("Added " + str(quantity) + " of " + item + " to your cart.")
            else:
                print("Sorry, we only have " + str(item_info['stock']) + " of " + item + " in stock.")
                self.add_cart()
        pass

    def remove_cart(self, item):
        """
        a mutator method used to remove an object from the user's cart using its item name and displays a message if
        the item was removed from the cart object
        :param item:
        :return:
        """
        try:
            self.shopping_cart.pop(item)
            print(f"{item} removed! ")
        except:
            print(f"{item} not in your cart! ")

    def edit_cart(self, item):
        """
        a mutator method used to decrement the amount of an item's amount the user wishes to order by asking the user
        how many of the item they would like to remove from their cart
        :param item:
        :return:
        """
        if item in self.shopping_cart:
            try:
                quantity = int(input('How many would you like to remove from your cart? '))
                if self.shopping_cart[item] >= quantity:
                    self.shopping_cart[item] -= quantity
                    if self.shopping_cart[item] <= 0:
                        del self.shopping_cart[item]
                    print("Removed " + str(quantity) + " of " + item + " from your cart.")
                else:
                    print("You only have " + str(self.shopping_cart[item]) + " of " + item + " in your cart.")
                    self.edit_cart(item)
            except:
                print('Please enter a valid number')
                self.edit_cart(item)
        else:
            print(item + " is not in your cart.")
        pass

    def checkout(self):
        """
        a mutator method used for when the user is ready to order the items in their cart
        this method calculates the total price of the user's cart and calls the inventory object's checkout method
        to decrement the store's inventory stock of each item in the user's cart by the amount of the item they selected

        :return:
        """
        ask = input('Are you sure you want to check out? y/n ')
        if str.upper(ask) == 'Y':
            total = 0
            for item, quantity in self.shopping_cart.items():
                item_info = self.store_inventory.get_item(item)
                if item_info:
                    if self.inventory_stock_validation(item, quantity):
                        total += item_info['cost'] * quantity
                        self.store_inventory.checkout({item: quantity})
                    else:
                        cart_quantity_adjustment = item_info['stock']
                        print(f'Your cart has been adjusted to reflect the amount of {item} stock.')
                        total += item_info['cost'] * cart_quantity_adjustment
                        self.store_inventory.checkout({item: cart_quantity_adjustment})
            print(f"Your total is ${total:,.2f}. Thank you for shopping with us!")
            self.shopping_cart.clear()
        pass

    def inventory_stock_validation(self, _item, _quantity):
        """
        inventory stock validation back up validation for while the user is checking out to ensure the inventory
        contains the amount the user selected
        :param _item: an item passed in from the user's shopping cart
        :param _quantity: the item's quantity from the user's shopping cart
        :return: returns either True or False depending on if the inventory currently holds the amount of stock the user
        has selected
        """
        if _quantity <= self.store_inventory.inventory[_item]['stock']:
            valid = True
            return True
        else:
            print(
                f"We're sorry the store only has {self.store_inventory.inventory[_item]['stock']} in stock at the moment")
            return False
