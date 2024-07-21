from inventory import Inventory
from cart import Cart


class Main(Cart):

    def __init__(self):
        super().__init__()

    def menu(self):
        """
        This function contains the main loop for the program that runs until the user decides to exit the program.
        The main loop contains the UI menu for the shopping website, enabling the user to select from
        showing the inventory, view their cart, add an item to their car, edit their cart, check out, and logout (exit)
        :return:
        """
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
        """
        function called to exit the program, also displays a message thanking the user for shopping with us today
        :return:
        """
        print('Thank you for shopping with us today!')
        exit()

    def inventory_menu(self):
        """
        sub inventory menu function. after showing the shops inventory displays another menu with all the options of the
        main menu excluding showing the inventory
        :return: nothing
        """
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
        """
        submenu function for viewing the cart. after showing the user's current cart displays another menu with all
        the options of the main menu excluding showing the view cart option
        :return: nothing
        """
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
        """
         Submenu function for editing the users cart. Give the user options for editing the contents of their cart
         :return: nothing
         """
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
        """
        submenu function for adding an item to the cart. Shows the current inventory for the user's convenience
        then calls the add_cart function.
        :return: nothing
        """
        self.store_inventory.get_inventory()
        self.add_cart()


m = Main()
m.menu()
