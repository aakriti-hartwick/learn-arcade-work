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
    # Create an empty list
    my_list = []
    kitchen = Room("kitchen a room with tasty chicken curry",'bedroom','south hall and Master room' , 'play hall','kitchen')
    bedroom = Room ("bedroom a room with bed and T.V" ,'Balcony', 'south hall and master room', 'play hall','kitchen')
    play_hall = Room("play hall a room with play station and football ", 'north hall and and bedroom','south hall and master bed room' ,'play hall')
    master_room = Room ('Master room with king size bed ', 'north hall and bedroom', "master room ", "play hall", 'kitchen ')

    # Create a player
    player = Player()







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
    # Create an empty list
    my_list ={}

    # Creating a variables for room named my_list

    my_list = [0,1,2,3,4]
    # Creating a string describing a room
    room_description = "You enter in a master bedroom which has king size bed and large window"

















