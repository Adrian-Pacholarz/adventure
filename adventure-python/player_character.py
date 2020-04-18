player_character = {
    # 'room': 'outside',
    'max_hp': 100
    'current_hp': 100
    'base_attack': 5
    'current_attack': 5
    'speed': 3 
}


def update_attack(player_status, inventory):
    if 'sword' in inventory:
        current_attack = base_attack + 3
    elif 'dagger' in inventory:
        current_attack = base_attack + 1


def print_status(player_status):
    pass