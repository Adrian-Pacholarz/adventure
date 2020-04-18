#import termcolor

player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.",
        "north": "cave",
        "movements": "There are the following exits: north"
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "south": "outside",
        "north": "room1",
        "movements": "There are the following exits: south, north"
    },
    "room1": {
        "title": "Room One",
        "description": "You're in a huge room inside the cave",
        "south": "cave",
        "east": "tunnel",
        "west": "catacombs",
        "movements": "There are the following exits: south, east, west"
    },
    "catacombs": {
        "title": "Entrance to catacombs",
        "description": "You're in an entrace to catacombs with many options to go further",
        "east": "room1",
        "west": "cave", # it goes back there
        "movements": "There are the following exits: east, west"
    },
    "tunnel": {
        "title": "Tunnel",
        "description": "You're in a small passage",
        "west": "cave",
        "north": "tunnel",
        "movements": "There are the following exits: west, north"
    }
}


def main():
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
            else:
                print(f'Unrecognized command: {command}')
        except KeyError:
            print(f'There is nothing there, current location is still: {player["room"]}')


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


if __name__ == '__main__':
    main()
