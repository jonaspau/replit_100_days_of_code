import random

def infinityDice(s):
  while True:
    print(random.randint(1,s))
    again = input("Roll again? ")
    if again == "y":
      continue
    else:
      print("Goodbye!")
      break


sides = int(input("How many sides?: "))
infinityDice(sides)