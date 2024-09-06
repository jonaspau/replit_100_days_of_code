import random

def rollDice(sides):
  return random.randint(1,sides)

print("--- CharacterGenerator ---")

while True:
  warrior = input("Name your warrior: ")
  dice1 = rollDice(6)
  dice2 = rollDice(8)
  hp = dice1 * dice2
  print(f"{dice1} x {dice2} = {hp}")
  print(f"{warrior} has an hp of {hp}!")
  newChar = input("another character? ")
  if newChar != "y":
    print("Sure, you don't need more heroes in your life!")
    break
  else:
    continue