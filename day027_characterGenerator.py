from random import randint
from time import sleep
from os import system


def generate_character():
  char_name = input("Name your character: ")
  char_type = input("Character Type (Human, Elf, Wizard, Orc): ") 
  health = get_health()
  strength = get_strengthac()
  return char_name, char_type, health, strength


def roll_dice(sides):
  return randint(1, sides)


def get_health():
  return roll_dice(6) * roll_dice(12) / 2 + 10


def get_strength():
  return roll_dice(6) * roll_dice(12) / 2 + 12


def main():
  while True:
    system("clear")
    print("Character Builder")
    print()
    char_name, char_type, health, strength = generate_character()
    print()
    print(char_name)
    print("HEALTH:", health)
    print("STRENGTH:", strength)
    print()
    print("May your name go down in Legend...")
    print()
    again = input("Again? (y/n): ")
    if again == "n":
      break

main()
