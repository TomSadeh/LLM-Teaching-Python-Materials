# Exercise 8: Build a Text Adventure with Classes!
#
# Put it all together to create an object-oriented text adventure game!


# ✏️ YOUR CODE HERE ✏️
# Create these classes for your adventure:


class Item:
    """An item that can be picked up and used"""

    def __init__(self, name, description, usable=True):
        # ✏️ YOUR CODE HERE ✏️
        pass

    def __str__(self):
        return self.name


class Room:
    """A location in the game"""

    def __init__(self, name, description):
        # ✏️ YOUR CODE HERE ✏️
        # self.name = name
        # self.description = description
        # self.items = []  # Items in this room
        # self.exits = {}  # {"north": another_room, "south": ...}
        pass

    def describe(self):
        # ✏️ YOUR CODE HERE ✏️
        # Print room name, description, items, and exits
        pass

    def add_exit(self, direction, room):
        # ✏️ YOUR CODE HERE ✏️
        pass


class Player:
    """The player character"""

    def __init__(self, name):
        # ✏️ YOUR CODE HERE ✏️
        # self.name = name
        # self.inventory = []
        # self.current_room = None
        # self.health = 100
        pass

    def move(self, direction):
        # ✏️ YOUR CODE HERE ✏️
        # Check if direction is a valid exit
        # If yes, move to that room
        # If no, print "You can't go that way!"
        pass

    def take(self, item_name):
        # ✏️ YOUR CODE HERE ✏️
        # Find item in current room
        # Add to inventory, remove from room
        pass

    def show_inventory(self):
        # ✏️ YOUR CODE HERE ✏️
        pass


class Game:
    """The main game controller"""

    def __init__(self):
        self.player = None
        self.rooms = {}
        self.running = True

    def setup(self):
        # ✏️ YOUR CODE HERE ✏️
        # Create rooms and connect them
        # Example:
        # entrance = Room("{{school}} Entrance", "You stand before the great doors...")
        # hall = Room("{{location}}", "Floating candles light the enormous room...")
        # entrance.add_exit("north", hall)
        # hall.add_exit("south", entrance)
        #
        # Add items to rooms
        # Set starting room
        pass

    def process_command(self, command):
        # ✏️ YOUR CODE HERE ✏️
        # Handle commands like:
        # - "go north" / "north" - move
        # - "take [item]" - pick up item
        # - "look" - describe room
        # - "inventory" / "i" - show inventory
        # - "quit" - end game
        pass

    def play(self):
        print("=" * 50)
        print("   WELCOME TO THE {{school}} ADVENTURE!")
        print("=" * 50)

        name = input("\nWhat is your name, young wizard? ")
        self.player = Player(name)
        self.setup()

        print(f"\n{{greeting}}, {name}!")
        print("Type 'help' for commands.\n")

        self.player.current_room.describe()

        while self.running:
            command = input("\n> ").lower().strip()
            if command:
                self.process_command(command)


def main():
    # To play the game, complete the classes above and uncomment:
    # game = Game()
    # game.play()

    print("Complete the classes above to play the adventure!")
    print("\nHere's a simpler working example:\n")

    # Mini working example
    class SimpleRoom:
        def __init__(self, name, desc):
            self.name = name
            self.desc = desc
            self.exits = {}

        def describe(self):
            print(f"\n=== {self.name} ===")
            print(self.desc)
            if self.exits:
                print("Exits:", ", ".join(self.exits.keys()))

    # Create two connected rooms
    start = SimpleRoom("{{school}} Gates",
                       "The magnificent gates of {{school}} tower before you.")
    hall = SimpleRoom("{{location}}",
                      "Torches line the stone walls. A grand staircase leads up.")

    start.exits["north"] = hall
    hall.exits["south"] = start

    current = start
    current.describe()

    # Simple game loop
    for _ in range(3):  # Just 3 moves for demo
        direction = input("\nWhere do you go? ")
        if direction in current.exits:
            current = current.exits[direction]
            current.describe()
        else:
            print("You can't go that way!")


main()
