import random
import os
from Player import Player
from PIL import Image

items = ["diamond ring", "key", "knife", "trap", "russian tank", "rose"]

inventory = []

description = {
    "Entrance": "Description: You are in the house entrance. There is a King Charles III painting, a (stolen) Banksy, a selfie stick, and doors to the north and east",
    "Garage": "Description: you are in a garage. Theres a new Tesla, a Benz and a Russian Tank. Also a door to the west and north.",
    "Halway": "Description: You are in a hallway. There are doors to the north, east, west and south.",
    "Garden": "Description: You are in a Garden. There are roses fertilizer and a corpse, and a door to the west and south,",
    "Master Bedroom": "Description: You are in a bedroom. There is a bed, a dresser and a key. There's a door to the south and a door to the west.",
    "Bathroom": "Description: You are in a bathroom. There is a sink, a toilet and a diamond ring, and a door to the south and east.",
    "Kitchen":"Description: You are in the kitchen there is a knife, a ham leg and fish and chips. There is a door to the east and to the north."
}

rooms = {
    "Entrance": {"east": "Garage", "north": "Halway"},
    "Garage": {"west": "Entrance", "north": "Garden"},
    "Halway": {"north": "Master Bedroom", "south": "Entrance", "east": "Garden", "west": "Kitchen"},
    "Garden": {"west": "Halway", "south": "Garage"},
    "Master Bedroom": {"south": "Halway", "west": "Bathroom"},
    "Bathroom": {"south": "Kitchen", "east": "Master Bedroom"},
    "Kitchen": {"east": "Halway", "north": "Bathroom"}
}

options = ["Move to a different room", "Find item", "quit"]

#Initialize player object
player = Player("Entrance")

# clears the terminal to make game more readable
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
# first menu player sees when starting the game. Gives option to show map or not
def menu():
    main_menu = input("Welcome to the dungeon!\n\nMap or no map? (y/n)")
    while True:
        if main_menu == "y":
            img = Image.open('map.PNG')
            img.show()
            break

        elif main_menu == "n":
            break

        else:
            print("Invalid input.")
            continue
    print("")


# displays the options the player has after every move
def prompt():
    print(f"you are in room {player.get_position()}\n{description[player.get_position()]}\n")
    print(f"Inventory: {inventory}")
    print("-------------------------")
    if len(inventory) == 4 and player.get_position() == "Lime":
        options.append("Open door")

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    print("-------------------------")
    print("")


# main game loop
def game_loop():

    # Randomizes item locations except for the item in the first room so the player doesn't get a trap instantly
    random.shuffle(items)
    item_location = {
    "Entrance": "",
    "Garage": items[0], 
    "Halway": items[1],
    "Garden": items[2],
    "Master Bedroom": items[3],
    "Bathroom": items[4],
    "Kitchen": items[5]
    }

    while True:

        prompt()
        next_move = (input("Next move: "))

        match(next_move):
            # movement of player in specific direction
            case "1":
                direction = input("where to you want to move? (Type: north, west, east or south)\n")

                clear()

                if direction in ["north", "west", "east", "south"]:

                    try: 
                        player.set_position(rooms[player.get_position()][direction])
                        print(f"you are in room {player.get_position()} \n{description[player.get_position()]}")

                    except KeyError:
                        print("Can't move in that direction.")

                else:
                    print("Invalid Input. Please enter 'north, west, east or south'.")

            # Picking up item
            case "2":

                clear()

                if item_location[player.get_position()] == "trap":
                    print("you have died.")
                    return False
                
                elif item_location[player.get_position()]:
                    print(f"you have found {item_location.get(player.get_position())}")
                    inventory.append(item_location.get(player.get_position()))
                    item_location[player.get_position()] = ""

                elif item_location[player.get_position()] == "":
                    print("You find nothing")
                    continue

            # Quitting the game
            case "3":
                break

            # Beating the game
            case "4":
                print("you have beaten the game!")
                break

            # Validating user input
            case _:
                clear()
                print("Please enter a valid input.\n")
                continue


def main():
    clear()
    menu()
    game_loop()

if __name__ == "__main__":
    main()