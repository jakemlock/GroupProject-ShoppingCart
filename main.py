from inventory import Inventory
from cart import Cart


class Main(Cart):

    def __init__(self):
        super().__init__()

    def menu(self):
        user_choice = None
        print(f'Welcome to Movie Website')

        while True:
            if user_choice == None:
                print(f'\nPlease select from the following menu then press enter')
                print(
                    f' 1) Show Inventory\n 2) View Cart\n 3) Add item to Cart\n 4) Edit Cart \n 5) Checkout\n 6) Logout')
                user_choice = int(input('Please enter your selection: '))
            if user_choice == 1:
                self.store_inventory.get_inventory()
                self.inventory_menu()
            elif user_choice == 2:
                # view cart function here
                self.get_cart()
                self.view_cart_menu()
            elif user_choice == 3:
                self.add_cart_menu()
            elif user_choice == 4:
                # edit cart function here
                self.edit_cart_menu()
            elif user_choice == 5:
                # checkout function here
                self.checkout()
            elif user_choice == 6:
                self.shut_down()
            else:
                print('You did not enter a valid command.')

            # resets user_choice for next iteration
            user_choice = None

    def shut_down(self):
        print('Thank you for shopping with us today!')
        exit()

    def inventory_menu(self):
        print(f'\nPlease select from the following menu then press enter')
        print(f'1) View Cart 2) Add item to Cart 3) Edit Cart 4) Checkout 5) Logout')
        _user_choice = int(input('Please enter your selection: '))
        if _user_choice == 1:
            # view cart function here
            self.get_cart()
        elif _user_choice == 2:
            self.add_cart_menu()
        elif _user_choice == 3:
            self.edit_cart_menu()
        elif _user_choice == 4:
            self.checkout()
        elif _user_choice == 5:
            self.shut_down()
        else:
            print('You did not enter a valid command.')

    def view_cart_menu(self):
        print(f'\nPlease select from the following menu then press enter')
        print(f'1) View Inventory 2) Add item to Cart 3) Edit Cart 4) Checkout 5) Logout')
        _user_choice = int(input('Please enter your selection: '))
        if _user_choice == 1:
            self.store_inventory.get_inventory()
        elif _user_choice == 2:
            self.add_cart_menu()
        elif _user_choice == 3:
            self.edit_cart_menu()
        elif _user_choice == 4:
            self.checkout()
        elif _user_choice == 5:
            self.shut_down()
        else:
            print('You did not enter a valid command.')

    def edit_cart_menu(self):
        self.get_cart()
        print(f'\nPlease select from the following menu then press enter')
        print(
            f' 1) Add item to Cart 2) Remove Item from Cart 3) Lower the Quantity of an Item in your cart 4)Checkout 5)Logout')
        _user_choice = int(input('Please enter your selection: '))
        if _user_choice == 1:
            self.add_cart_menu()
        elif _user_choice == 2:
            item = input('Which item would you like to remove? ')
            self.remove_cart(item)
        elif _user_choice == 3:  #
            self.get_cart()
            item = input('Which item would you like to edit? ')
            self.edit_cart(item)
        elif _user_choice == 4:
            self.checkout()
        elif _user_choice == 5:
            self.shut_down()
        else:
            print('You did not enter a valid command.')

    def add_cart_menu(self):
        self.store_inventory.get_inventory()
        self.add_cart()


m = Main()
m.menu()
