import termcolor

player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.",
        "movemnets": "norht"
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
    },
}


def main():
    describe_room()
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
        elif command in ['quit', 'q']:
            print('Bye!')
            playing = False
        elif command in ['north',  'n']:
            pass
        elif command in ['south', 's']:
            pass
        elif command in ['east', 'e']:
            pass
        elif command in [ 'west', 'w']:
            pass
        else:
            print(f'Unrecognized command: {command}')


def get_command():
    print()
    return input('> ')


def describe_room():
    room = rooms[player['room']]
    print()
    print(room['title'])
    print()
    print(room['description'])


if __name__ == '__main__':
    main()
