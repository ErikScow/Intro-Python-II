from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

Player1 = Player("You", 'outside')

def currentLocation():
    return f"Your current location is the {room[Player1.current_room].name}\n{room[Player1.current_room].description}"

print(currentLocation())

cmd = input('Please select your action\n[n] go north\n[w] go west\n[s] go south\n[e] go east\n[q] quit\n')

while not cmd == 'q':
    if cmd == 'n' or cmd == 'w' or cmd == 's' or cmd == 'e':
        if cmd == 'n':
            try:
                Player1.change_room(room[Player1.current_room].n_to)
                print(currentLocation())
            except AttributeError:
                print('Nothing that way! Pick a different direction!')
                pass
        elif cmd == 'w':
            try:
                Player1.change_room(room[Player1.current_room].w_to)
                print(currentLocation())
            except AttributeError:
                print('Nothing that way! Pick a different direction!')
                pass
        elif cmd == 's':
            try:
                Player1.change_room(room[Player1.current_room].s_to)
                print(currentLocation())
            except AttributeError:
                print('Nothing that way! Pick a different direction!')
                pass
        elif cmd == 'e':
            try:
                Player1.change_room(room[Player1.current_room].e_to)
                print(currentLocation())
            except AttributeError:
                print('Nothing that way! Pick a different direction!')
                pass
    elif cmd == 'other inputs not yet valid':
        print('These commands dont do anything yet, wait for future updates')
    else:
        print('Please enter a valid command')

    cmd = input('Please select your action\n[n] go north\n[w] go west\n[s] go south\n[e] go east\n[q] quit\n')
        