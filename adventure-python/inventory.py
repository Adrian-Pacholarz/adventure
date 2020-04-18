
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

# modules------------------------------------------
import terminal_view
import os

# global variables--------------------------------- 
INVENTORY = {}
INVENTORY_PATH = "/home/lukasz-lesiuk/codecool/rougelike/game-inventory-lukasz-lesiuk/inventory.csv"


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way.
    
    Args: 
    dict - inventory to show 
    """
    if inventory:
        for item, qty in inventory.items():
            print(f"{item}: {qty}")


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items.
    
    Args:
    dict - target inventory
    list - items to add to dictionary
    
    Return:
    dict - updated dictionary"""

    for item in added_items: 
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else: 
            inventory[item] = 1
    
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items.
    
        Args:
    dict - target inventory
    list - items to add to dictionary
    
    Return:
    dict - updated dictionary"""
    
    for item in removed_items: 
        if item in inventory:
            inventory[item] = inventory[item] - 1

    keys_to_delete = []
    for item in inventory:
        if inventory[item] == 0:
            keys_to_delete.append(item)
    
    for item in keys_to_delete:
        del inventory[item]
    
    return inventory


def import_inventory(inventory, filename = 'inventory.csv'):
    """Import new inventory items from a CSV file.

    Args:
    dict - to which import items from csv 
    string - adress of csv file with inventory

    Return:
    dict - containing items in dictionary
    
    """

    try:
        with open(filename, "r") as file:
            items = file.read().split(",")
        for item in items: 
            if item in inventory:
                inventory[item] = inventory[item] + 1
            else: 
                inventory[item] = 1

    except FileNotFoundError:
        print("File 'no_such_file.csv' not found!")

    return inventory


def save_item(item, qty, filename):
    """ Writes item name specified numbers of time to file
    
    Args:
    str - item name
    int - item qty
    str - file to which save data """
    
    string_to_write = item

    while qty > 0:
        with open(filename, 'a') as file:
            file.write((string_to_write))
        string_to_write = "," + item
        qty = qty - 1


def export_inventory(inventory, filename = "export_inventory.csv"):
    """Export the inventory into a CSV file.
    
    Args:
    dictionary - containing inventory
    str - filename, by default 'export_inventory.csv'
    """

    try:
        open(filename, 'w').close()
    
        for item, qty in inventory.items():
            if not os.stat(filename).st_size == 0:
                save_item(",",1 , filename)
            save_item(item, qty, filename)
    
        print("Save succesful")

    except IOError:
        print("You don't have permission creating file '/nopermission.csv'!")


def print_table(inventory, order = 'empty'):
    terminal_view.print_table(inventory, order)


def main():

    import_inventory(INVENTORY)

    to_add = ['alpaca', 'alpaca', 'dagger', 'lama', 'lama']
    add_to_inventory(INVENTORY, to_add)

    # terminal_view.print_table(INVENTORY)
    # import_inventory(INVENTORY, INVENTORY_PATH)

    print_table(INVENTORY, "count,desc")
    export_inventory(INVENTORY)


if __name__ == '__main__':
    main()

