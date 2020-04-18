import terminal_view

# TEMP
INVENTORY = {'dagger', 'lama'}


player_character = {
    # 'room': 'outside',
    'max_hp': 100,
    'current_hp': 100,
    'base_attack': 5,
    'current_attack': 5,
    'speed': 3 
}


def update_attack(player_status, inventory):
    if 'sword' in inventory:
        player_character['current_attack'] = player_character['base_attack'] + 3
    elif 'dagger' in inventory:
        player_character['current_attack'] = player_character['base_attack'] + 1


def print_status(player_status):
    pass



if __name__ == '__main__':
    terminal_view.print_table(player_character)
    update_attack(player_character, INVENTORY)
    terminal_view.print_table(player_character)