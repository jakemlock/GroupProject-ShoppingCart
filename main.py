from inventory import Inventory


def main():
    user_choice = 0
    store_inventory = Inventory()
    print(f'Welcome to shopping website')
    while user_choice != 6:
        user_choice = menu()
        if user_choice == 1:
            store_inventory.get_inventory()
        elif user_choice == 2:
            # view cart function here
            pass
        elif user_choice == 3:
            add_item_to_cart(store_inventory)
        elif user_choice == 4:
            # edit cart function here
            pass
        elif user_choice == 5:
            # checkout function here
            pass
        else:
            print('You did not enter a valid command.')
            user_choice = menu()


def menu():
    # main menu-- number system?  1) view cart, 2)add item, etc...
    print(f'Please select from the following menu then press enter')
    print(f' 1) Show Inventory\n 2) View Cart\n 3) Add item to Cart\n 4) Edit Cart \n 5) Checkout\n 6) Close site')
    user_choice = int(input('Please enter your selection: '))
    return user_choice


def add_item_to_cart(_inventory):
    _inventory.get_inventory()
    item = input('Please type in the item you would like to add to your cart: ')
    item_to_add = _inventory.get_item(item)
    if item_to_add:
        count_of_item = int(input('How many would you like to add to your cart? '))
        if count_of_item < item_to_add['stock']:
            print(f"{item}: Cost: ${float(item_to_add['cost']):,.2f}")
            # add item to cart object here
        else:
            print(f"We're sorry we only have {item_to_add['stock']} Available at the moment")


if __name__ == "__main__":
    main()
