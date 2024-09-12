from os import system
from time import sleep

appTitle = "Star Wars name generator"

def main():
    while True:
        system("clear")
        print(f"--- {appTitle}---\n")
        firstName, lastName, maidenName, city = getInput()
        starwarsName = starWars_name(firstName, lastName, maidenName, city)
        print(f"Your Star Wars name is {starwarsName}\n")
        if not again():
            print(f"Goodbye {starwarsName}")
            sleep(2)
            break


def starWars_name(first, last, maiden, city):
    new_first = f"{first[:3].title()}{last[:3].lower()}"
    new_last = f"{maiden[:2].title()}{city[-3:].lower()}"
    starWarsed = f"{new_first} {new_last}"
    return starWarsed


def getInput():
    first = input("Enter your first name: ").strip()
    last = input("Enter your last name: ").strip()
    maiden = input("Enter your mother's maiden name: ").strip()
    city = input("Enter the city where you were born: ").strip()
    return first, last, maiden, city


def again():
    again = input("Generate another name (y/n)? ").lower()
    print()
    if again == "y":
        return True
    else:
        return False


main()