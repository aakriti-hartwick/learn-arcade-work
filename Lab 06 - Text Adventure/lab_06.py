class Room:
    """
    This is a class that represents the player character.
    """
    def __init__(self, description, north, south, east, west):
        """ This is a method that sets up the variables in the object. """
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []

    room = Room("You are in master-bedroom with king size bed.", 1, None, 6, None)
    room_list.append(room)

    room = Room("You are in kitchen and chicken fries are being cooked.", None, 0, 2, None)
    room_list.append(room)

    room = Room("You are in north hall.", None, 6, 3, 1)
    room_list.append(room)

    room = Room("You are in bed-room.", None, 4, None, 2)
    room_list.append(room)

    room = Room("Play hall with play station and football.", 3, None, None, 6)
    room_list.append(room)

    room = Room("You are in garden where flowers are blooming.", 6, None, None, None)
    room_list.append(room)

    room = Room("You are at south hall.", 2, 5, 4, 0)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print()

        print(room_list[current_room].description)

        user_input = input("What do you want to do? "). lower()

        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("\n You can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("\n You can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("\n You can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("\n You can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("\nThank you for playing. See you again.")
            done = True

        else:
            print("\nDidn't get you. Try again.")


main()