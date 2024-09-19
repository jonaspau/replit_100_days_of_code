import os
import time

backpack = []


def main():
    loadFile()
    while True:
        option = showMenu()
        if option == "1":
            addItem()
        elif option == "2":
            useItem()
        elif option == "3":
            viewItems()
        elif option == "q":
            os.system("clear")
            break
        time.sleep(1)
        os.system("clear")


def showMenu():
    print("--- RPG inventory! ---\n")
    print("1: Add to backpack")
    print("2: Use")
    print("3: View items")
    print("q: Quit")
    print()
    option = input("Option: ").lower()
    return option


def addItem():
    item = input("What would you like to add to the backpack? ").strip().title()
    backpack.append(item)
    print(f"Added {item} to the backpack.")
    saveFile()


def useItem():
    item = input("What would you like to use? ").strip().title()
    if item in backpack:
        backpack.remove(item)
        saveFile()
    else:
        print(f"You have no {item} in your backpack")


def viewItems():
    inventory = {}
    for item in backpack:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    os.system("clear")
    print("--- RPG inventory! ---\n")
    for item, qty in inventory.items():
        print(f"{item:<10}{qty:>5}")
    time.sleep(3)


def loadFile():
    global backpack
    try:
        with open("backpack.txt", "r") as f:
            backpack = eval(f.read())
    except FileNotFoundError:
        print("Could not load inventory, starting with an empty backpack.\n")
        backpack = []
    except Exception as err:
        print("An error occured")


def saveFile():
    try:
        with open("backpack.txt", "w") as f:
            f.write(str(backpack))
    except Exception as err:
        print("Error saving to file.")


main()
