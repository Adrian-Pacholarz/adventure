import terminal_view

# TEMP
INVENTORY = {'dagger', 'lama'}


player_character = {
    # 'room': 'outside',
    'max_hp': 100,
    'current_hp': 100,
    'base_attack': 5,
    'current_attack': 5,
    'base_speed': 3,
    'current_speed': 3
}


def update_status(player_status, inventory):
    if 'sword' in inventory:
        player_character['current_attack'] = player_character['base_attack'] + 3
    elif 'dagger' in inventory:
        player_character['current_attack'] = player_character['base_attack'] + 1

    if 'lama' in inventory:
        player_character['current_speed'] = player_character['base_speed'] + 10


    if player_status['current_hp'] > 100:
        player_status['current_hp'] = 100
    elif player_status['current_hp'] <= 0:
        print("YOU DIED")
        quit()


if __name__ == '__main__':
    terminal_view.print_table(player_character)
    update_status(player_character, INVENTORY)
    terminal_view.print_table(player_character)
