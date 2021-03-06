import inventory
import player_character
import characters
import combat
import random
import terminal_view
# global variables------------------------
INVENTORY = {}
# PLAYER_STATUS

player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.",
        "north": "cave",
        "movements": "There are the following exits: north",
        "items": [],
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "south": "outside",
        "north": "room1",
        "movements": "There are the following exits: south, north",
        "items": [],
    },
    "room1": {
        "title": "Room One",
        "description": "You're in a huge room inside the cave",
        "south": "cave",
        "east": "tunnel",
        "west": "catacombs",
        "north": "dungeons",
        "movements": "There are the following exits: north, south, east, west",
        "items": ["sword"],
    },
    "catacombs": {
        "title": "Entrance to catacombs",
        "description": "You're in an entrace to catacombs with many options to go further",
        "east": "room1",
        "west": "outside", # it goes back there
        "movements": "There are the following exits: east, west",
        "items": ["gold key"],
    },
    "tunnel": {
        "title": "Tunnel",
        "description": "You're in a small passage",
        "west": "cave",
        "north": "tunnel",
        "movements": "There are the following exits: west, north",
        "items": [],
    },
    "dungeons": {
        "title": "Dungeons",
        "description": "You'll never get out of the dungeons",
       "south": "secret room",
        "east": "dungeons",
        "west": "dungeons",
        "north": "dungeons",
        "movements": "There are the following exits: north, south, east, west",
        "items": [],
    },
}

random_place = random.choice(list(rooms.keys()))
ghost = {
    'room:': random_place
}

def open_door(playing = True):
    if "gold key" in INVENTORY:
        print("You win!!!")
        playing = False
    else:
        print("You don't have a key")
        player['room'] = "outside"
    return playing


def get_help():
    print("HELP MENU:")
    help_option = ("look/l - look up around",
                    "north/n - go to north",
                    "south/s - go to south",
                    "east/e - go to east",
                    "west/w - go to west",
                    "get/g - add item to you bag",
                    "bag/b - bag preview",
                    "quit/q - quit the game")
    for help in help_option:
        print(f"    {help}")


def ask_riddle():
    print("Who is the best funny actor in the world?")
    if get_command() == "Jim Carrey":
        inventory.add_to_inventory(INVENTORY, rooms[player['room']]["items"])
        print(f"You get item {rooms[player['room']]['items']}")
        rooms[player['room']]["items"] = []
    else:
        player['room'] = "outside"
        print("Answer is incorrect! You are kick up on the outside.")


# def if player['room'] == ghost['room']:
    pass


def main():
    # inventory.import_inventory(INVENTORY)
    # inventory.print_table(INVENTORY)
    describe_room()
    playing = True
    while playing:
        command = get_command().lower()
        try:
            if command in ['look', 'l']:
                describe_room()
            elif command in ['quit', 'q']:
                print('Bye!')
                playing = False
            elif command in ['north',  'n']:
                player['room'] = rooms[player['room']]["north"]
                describe_room()
            elif command in ['south', 's']:
                player['room'] = rooms[player['room']]["south"]
                describe_room()
            elif command in ['east', 'e']:
                player['room'] = rooms[player['room']]["east"]
                describe_room()
            elif command in [ 'west', 'w']:
                player['room'] = rooms[player['room']]["west"]
                describe_room()
            elif command in [ 'get', 'g']:
                if player['room'] == 'catacombs':
                    ask_riddle()
                else:
                    inventory.add_to_inventory(INVENTORY, rooms[player['room']]["items"])
                    rooms[player['room']]["items"] = []
            elif command in [ 'bag', 'b']:
                if INVENTORY:
                    inventory.print_table(INVENTORY)
            elif command in [ 'help', 'h']:
                get_help()
            elif command in ['status']:
                terminal_view.print_table(player_character.player_character)
            else:
                print(f'Unrecognized command: {command}')
            
        except KeyError:
            print(f'There is nothing there, current location is still: {player["room"]}')
    
        ghost_movement()
        if player['room'] == 'secret room':
            playing = open_door()


def get_command():
    print()
    return input('> ')


def describe_room():
    room = rooms[player['room']]
    print()
    print(room['title'])
    print()
    print(room['description'])
    print(room["movements"])
    if room["items"]:
        print(f'The following items on the ground: {room["items"]}')


def ghost_movement():
    random_place = random.choice(list(rooms.keys()))
    ghost = {
            'room': random_place
            }
    if player['room'] == ghost['room']:
        character = characters.characters["ghost"]
        print(character["description"])
        print("BEGIN COMBAT")
        combat.combat(player_character.player_character, characters.characters["ghost"])


if __name__ == '__main__':
    main()
