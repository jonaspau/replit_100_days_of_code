import random
import os

words = ["python", "javascript", "programming", "computer", "science", "mathematics", "engineering", "technology", "artificial", "intelligence"]

word = random.choice(words)
all_letters = []
guessed_letters = []
lives = 6  

def main():
  
  allLetters()
  while True:
    printGallows()
    printWord()
    print(f"Lives: {lives}")
    print()
    letter = guessLetter()
    checkLetter(letter)

    if lives == 0:
      printGallows()
      print("You lost!")
      print(f"The word was {word}")
      break
    elif sorted(all_letters) == sorted(guessed_letters):
      print("Yay! You won!")
      break


def guessLetter():
  letter = input("Guess a letter: ").strip().lower()
  if len(letter) != 1:
    print("Only one letter allowed.")
    guessLetter()
  else:
    return(letter)
  

def checkLetter(letter):
  global lives
  global guessed_letters

  if letter in guessed_letters:
    print("You already guessed that letter.")
  elif letter in word:
    print("Correct!")
    guessed_letters.append(letter)
    guessed_letters = guessed_letters
  else:
    print("Incorrect!")
    lives -= 1


def printWord():
  global word
  global guessed_letters
  for letter in word:
    if letter in guessed_letters:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print()


def allLetters():
  global word
  global all_letters
  
  for letter in word:
    if letter not in all_letters:
      all_letters.append(letter)  

def printGallows():
  global lives
  os.system("clear")
  print("--- Hangman ---")
  if lives == 6:
    print("  _______ ")
    print("  |     | ")
    print("  |       ")
    print("  |       ")
    print("  |       ")
  elif lives == 5:
    print("  _______ ")
    print("  |     | ")
    print("  |     O ")
    print("  |       ")
    print("  |       ")
  elif lives == 4:
    print("  _______ ")
    print("  |     | ")
    print("  |     O ")
    print("  |     0 ")
    print("  |       ")
  elif lives == 3:
    print("  _______ ")
    print("  |     | ")
    print("  |     O ")
    print("  |    /0 ")
    print("  |       ")
  elif lives == 2:
    print("  _______  ")
    print("  |     |  ")
    print("  |     O  ")
    print("  |    /0\\")
    print("  |        ")
  elif lives == 1:
    print("  _______  ")
    print("  |     |  ")
    print("  |     O  ")
    print("  |    /0\\")
    print("  |    /   ")
  elif lives == 0:
    print("  _______  ")
    print("  |     |  ")
    print("  |     O  ")
    print("  |    /0\\")
    print("  |    / \\ ")
  print()


main()