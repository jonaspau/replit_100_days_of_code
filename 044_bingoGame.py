from random import randint
from os import system

picked = []

def main():
    
  numbers = generate_numbers()
  card = format_bingo_card(numbers)
  numbers_left = 8
  while True:
    print("--- BINGO ---\n")
    print_bingo_card(card)
    numbers_left = getNumber(picked, card, numbers_left)
    
    system("clear")
    
    if numbers_left == 0:
      print("--- BINGO ---\n")
      print_bingo_card(card)
      print("BINGO!\nCongratulations, you Won")
      break


def generate_numbers():
  numbers = []
  while len(numbers) < 8:
    num = randint(1, 90)
    if num not in numbers:
      numbers.append(num)
  numbers = sorted(numbers)
  return numbers


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


def getNumber(picked, card, numbers_left):
  num = int(input("Enter a number: "))
  if num not in picked:
    picked.append(num)
    for row in card:
      if num in row:
        row[row.index(num)] = "X"
        numbers_left -= 1
        return numbers_left
    return numbers_left

if __name__=="__main__":
  main()