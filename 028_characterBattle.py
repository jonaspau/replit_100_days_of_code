from random import randint
from time import sleep
from os import system


def generate_character():
  char_name = input("Name your character: ")
  char_type = input("Character Type (Human, Elf, Wizard, Orc): ") 
  health = get_health()
  strength = get_strength()
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
    print("Battle Time", "\n")
    
    # generate character 1
    char1_name, char1_type, char1_health, char1_strength = generate_character()
    print(f"{char1_name} the {char1_type}")
    print(f"Health: {char1_health}")
    print(f"Strength: {char1_strength}\n")

    # generate character 2
    char2_name, char2_type, char2_health, char2_strength = generate_character()
    print(f"{char2_name} the {char2_type}")
    print(f"Health: {char2_health}")
    print(f"Strength: {char2_strength}\n")

    sleep(2)
    system("clear")
    
    # battle
    print("Battle Begins!")
    sleep(2)
    system("clear")
    
    rounds = 0
    while char1_health > 0 and char2_health > 0:
      rounds += 1
      sleep(2)
      system("clear")
      print(f"Round {rounds}")
      char1_roll = roll_dice(6)
      char2_roll = roll_dice(6)
      
      if char1_roll > char2_roll:
        damage = abs(char1_strength - char2_strength) + 1
        char2_health -= damage
        print(f"{char2_name} takes a hit, with {damage} damage")
        print(f"{char1_name} wins the round\n")

      elif char1_roll < char2_roll:
        damage = abs(char2_strength - char1_strength) + 1
        char1_health -= damage
        print(f"{char1_name} takes a hit, with {damage} damage")
        print(f"{char2_name} wins the round\n")

      else:
        print("It's a tie")
      
      print(f"{char1_name} the {char1_type}")
      print(f"Health: {char1_health}\n")
      print(f"{char2_name} the {char2_type}")
      print(f"Health: {char2_health}\n")

      if char1_health <= 0 or char2_health <=0:
        break

    if char1_health > 0:
      print(f"{char1_name} the {char1_type} wins!")
      loser = char2_name
    else:
      print(f"{char2_name} the {char2_type} wins!")
      loser = char1_name
    print(f"It took {rounds} rounds to annihilate {loser}")
    
    again = input("Play again? (y/n): ").lower()
    if again == "n":
      break

main()
