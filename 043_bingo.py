from random import randint
from os import system


def main():
  while True:
    print("--- Bingo Card Generator ---")
    print()
    print_bingo_card(generate_numbers())
    print()
    again = input("Do you want to generate another card? (y/n): ")
    if again.lower() != "y":
      break
    else:
      system("clear")
  

def generate_numbers():
  numbers = []
  while len(numbers) < 8:
    num = randint(1, 90)
    if num not in numbers:
      numbers.append(num)
  numbers = sorted(numbers)
  card = format_bingo_card(numbers)
  return card


def format_bingo_card(nums):
  card = [
    [nums[0], nums[1], nums[2]],
    [nums[3], "BINGO", nums[4]],
    [nums[5], nums[6], nums[7]]
  ]
  return card


def print_bingo_card(card):
  print("-" * 24)
  for row in card:
    print("|", end="")
    for num in row:
      print(f"{num:^5}", end=" | ")
    print()
    print("-" * 24)


if __name__=="__main__":
  main()