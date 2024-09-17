import random
import os

cards = {}
cards["JP"] = {
  "IQ": 183,
  "Skills": 30,
  "Teaching": 100
}
cards["David"] = {
  "IQ": 179,
  "Skills": 90,
  "Teaching": 90
}
cards["Malan"] = {
  "IQ": 200,
  "Skills": 100,
  "Teaching": 200
}


def checkWinner():
  if cards[player][answer] > cards[computer][answer]:
    print("Player wins")
  elif cards[player][answer] < cards[computer][answer]:
    print("Computer wins")
  else:
    print("It's a tie")
  print()


def printCards():
  print("Cards")
  for key in cards:
    print(key)
  print()


def pickCards():
  player = input("Pick a card: ")
  computer = random.choice(list(cards.keys()))
  return(player, computer)


def pickSkill():
  answer = input("Choose your stat (IQ, Skills, Teaching): ")
  print(f"{player}: {cards[player][answer]}")
  print(f"{computer}: {cards[computer][answer]}\n")
  return(answer)
  

while True:
  printCards()
  player, computer = pickCards()
  print(f"Player's choice: {player} - Computer's choice {computer}\n")
  answer = pickSkill()
  checkWinner()

  again = input("Play again? y/n: ")
  if again == "n":
    break
  os.system("clear")