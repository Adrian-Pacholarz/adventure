def print_bar(length):
    """Prints row consisting of specified numbers of "-"
    Args:
    int - length og bar
    """
    for symbol in range(length):
        print("-", end="")
    print("")


def print_spacing(height):
    """ Print spiecified number of empty lines
    
    Args:
    int - number of empty lines """
    
    for row in range(height):
        print("", end="\n")


def print_inventory_row(item, qty, longest_item_len, longest_qty_len, separator):
    """ Print row of specified length, with item name and item qty
    
    Args:
    string - item name from inventory
    string - quantity of item
    int    - no. of whitespaces before item
    int    - no. of whitedpaces before qty
    string - separator dividing two elements """
       
    item_filler = ""
    qty_filler = ""

    item_spacing = longest_item_len - len(item)
    qty_spacing = longest_qty_len - len(str(qty))

    for symbol in range(item_spacing):
        item_filler += " "

    for symbol in range(qty_spacing):
        qty_filler +=" "

    row = item_filler + item + " | " + qty_filler + str(qty)
    print(row)


def print_table(inventory, order = 'empty'):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.

    Args:
    dict - inventory to print
    string - set printing order as follows:
      * empty (by default) means the table is unordered
    * `count,desc` means the table is ordered by count (of items in the inventory) in descending order
    * `count,asc` means the table is ordered by count in ascending order
    """

    separator = " | "
    item_header = "item name"
    qty_header = "count"
    longest_item_len = len(item_header)
    longest_qty_len = len(qty_header)

    for item, qty in inventory.items():
        if len(item) > longest_item_len:
            longest_item_len = len(item)
        if len(str(qty)) > longest_qty_len:
            longest_qty_len = len(str(qty))
    
    total_length = longest_item_len + longest_qty_len + len(separator)
    
    print_bar(total_length)
    print_inventory_row("item name", "count", longest_item_len, longest_qty_len, separator)
    print_bar(total_length)
    
    if order == 'count,asc':
        for item, qty in sorted(sorted(inventory.items()), key=lambda x: x[1]):
            print_inventory_row(item, qty, longest_item_len, longest_qty_len, separator)
    elif order == 'count,desc':
        for item, qty in sorted(sorted(inventory.items()),reverse=True, key=lambda x: x[1]):
            print_inventory_row(item, qty, longest_item_len, longest_qty_len, separator)
    else:
        for item, qty in inventory.items():
            print_inventory_row(item, qty, longest_item_len, longest_qty_len, separator)

    print_bar(total_length)