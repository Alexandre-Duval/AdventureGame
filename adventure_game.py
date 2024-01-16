import random
from Player import Player
import os


items = ["banana", "key", "skull", "potion", "sword"]
inventory = []
description = {
    "Red": "Description: Red Room",
    "Pink": "Description: Pink Room",
    "Orange": "Description: Orange Room",
    "Blue": "Description: Blue Room",
    "Lime": "Description of Lime Room",
}

rooms = {
    "Red": {"East": "Pink"},
    "Pink": {"South": "Green", "West": "Red", "East": "Orange"},
    "Green": {"North": "Pink"},
    "Orange": {"West": "Pink", "East": "Blue", "North": "Lime"},
    "Blue": {"West": "Orange"},
    "Lime": {"South": "Orange"},
}

player = Player(100, "Red")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    main_menu = input("Welcome to the dungeon!\n\nMap or no map? (y/n)")
    while True:
        if main_menu == "y":
            "display map"
            break
        elif main_menu == "n":
            break
        else:
            print("not valid input")
            continue
    print(f"you are in room {player.get_position()}\n{description[player.get_position()]}\n")


def move():
    input("where to you want to move?")
    if direction  in ["north", "west", "east", "south"]:
        player.set_position(rooms[player.get_position()][direction.capitalize().split(" ")])
        print( f"you are in room {player.get_position()}\n{description[player.get_position()]}")
    else:
        print("Invalid Input. Please enter 'north, west, east or south'.")


def prompt():
    print(f"Location: {player.get_position()}")
    print(f"Inventory:{inventory}")
    print("--------\n")


def main():
    random.shuffle(items)
    item_location = {
        "Red": items[0],
        "Pink": items[1],
        "Orange": items[2],
        "Blue": items[3],
        "Lime": items[4],
    }

    menu()

    while True:
        prompt()

        next_move = input("Next move:\n")

        if next_move == "move":
            move()

        if next_move == "find item":
            if item_location[player.get_position()]:
                print(f"you have found a {item_location.get(player.get_position())}")
                inventory.append(item_location.get(player.get_position()))
                item_location[player.get_position()] = ""

            elif item_location[player.get_position()] == "":
                print("You find nothing")
                continue


main()
