### Helper functions for displaying rooms ###

def show_room_0():
    """Display the contents of room 0."""
    print("You are in an empty room with white walls.")
    print("There are no exits.")

def show_room(room_num):
    """Display the contents of the given room.
    Input:
    - room_num : int, the number of the room to show.
    """
    if room_num == 0:
        show_room_0()
    else:
        print("You are out of bounds. Room", room_num, "does not exist.")

### The main game loop ###

def game_loop():
    """Main loop of the game - this is where the fun happens."""

    # We start in room 0
    current_room = 0

    # Display the room that we start in
    show_room(current_room)

    # Enter the main loop, where the user can input commands.
    while True:
        user_inp = input("> ")

        if user_inp == "quit":
            break
        else:
            print("I do not understand the command:", user_inp)

# Start the game!
game_loop()
