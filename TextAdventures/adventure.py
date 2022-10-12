### Helper functions for displaying rooms ###

def show_room_0():
    """Display the contents of room 0."""
    print("You are in a cold, damp basement.")
    print("North of you is a staircase leading up.")

def show_room_1():
    """Display the contents of room 1."""
    print("You are in an abandoned entry hall. It's full of broken furniture.")
    print("South of you is a staircase leading down.")
    print("There are doors to the east and west.")
    print("North of you is a grand double door, perhaps leading outside,")
    print("but when you pull the handle, it doesn't open.")

def show_room_2():
    """Display the contents of room 2."""
    print("You are in a grand dining hall. In the center of the room is a long")
    print("table of dark polished wood, set with the finest porcelain and")
    print("silverware. At the end of the table stands a grand throne-like")
    print("chair.")
    print("To the west is a door.")

def show_room_3():
    """Display the contents of room 3."""
    print("You are in a cozy sitting room. At the western wall is a hearth,")
    print("currently cold. The ashes haven't been swept away. By the hearth")
    print("are three soft leather chairs. The walls are lined with bookcases,")
    print("though the few remaining books smell musty, half-eaten by mice.")
    print("East of you is a door.")

def show_room(room_num):
    """Display the contents of the given room.
    Input:
    - room_num : int, the number of the room to show.
    """
    if room_num == 0:
        show_room_0()
    elif room_num == 1:
        show_room_1()
    elif room_num == 2:
        show_room_2()
    elif room_num == 3:
        show_room_3()

### Movement, depending on what room we're in. ###

def move_from_0(direction):
    """Movement if we are currently in room 0."""
    if direction == "north":
        print("You walk up the staircase, avoiding some rubble halfway up.")
        print("Upstairs is a door leading into an entry hall.")
        return 1
    return 0

def move_from_1(direction):
    """Movement if we are currently in room 1."""
    if direction == "south":
        print("You walk down the stairs into the basement.")
        return 0
    elif direction == "east":
        print("You walk through the door into a dining hall.")
        return 2
    elif direction == "west":
        print("You walk through the door into a sitting room.")
        return 3
    elif direction == "north":
        print("The door appears to be locked, or perhaps rusted shut.")
        return 1
    return 1

def move_from_2(direction):
    """Movement if we are currently in room 2."""
    if direction == "west":
        print("You walk through the door to the entry hall.")
        return 1
    return 2

def move_from_3(direction):
    """Movement if we are currently in room 3."""
    if direction == "east":
        print("You walk through the door to the entry hall.")
        return 1
    return 3

def move(current_room, direction):
    """Movement from current room."""
    new_room = current_room
    if current_room == 0:
        new_room = move_from_0(direction)
    elif current_room == 1:
        new_room = move_from_1(direction)
    elif current_room == 2:
        new_room = move_from_2(direction)
    elif current_room == 3:
        new_room = move_from_3(direction)

    if new_room == current_room:
        print("There is no exit there.")

    return new_room

### "OOC" stuff ###

def show_help():
    print("Commands:")
    print("quit : Exits the game")
    print("look : Look around the room you're in")
    print("move : Go somewhere, for example 'move north'")

### The main game loop ###

def game_loop():
    """Main loop of the game - this is where the fun happens."""

    # We start in room 0
    current_room = 0

    # Display the room that we start in
    show_room(current_room)

    # Enter the main loop, where the user can input commands.
    while True:
        user_inp = input("> ").lower()

        if user_inp == "quit":
            break
        elif user_inp == "help":
            show_help()
        elif user_inp == "look":
            show_room(current_room)

        # Handle movement commands:
        elif user_inp[:4] == "move":
            # if the user has entered, for example, 'move north', we want to extract
            # the word 'north' - we do that by removing the first 5 letters (m, o, v, e, space).
            direction = user_inp[5:]

            # Based on the current room, and the direction calculated above, we determine what room we
            # end up in, and update the current_room variable to reflect this.
            current_room = move(current_room, direction)

        else:
            print("I do not understand the command:", user_inp)

# Start the game!
game_loop()
