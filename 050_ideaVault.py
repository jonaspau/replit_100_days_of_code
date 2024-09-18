# Get an idea
# Save it to a file my.ideas on a new line
# Show a menu letting users add a new idea, or show a random idea
import os
import random
import time


def main():
  while True:
    os.system("clear")
    menu = input("1: Add a new idea\n2: Show a random idea\nQ: Exit\nOption: ").lower()
    if menu == "1":
      addIdea()
    elif menu == "2":
      showIdea()
    elif menu == "q":
      os.system("clear")
      break


def addIdea():
  f = open("my.ideas", "a+")
  idea = input("What's the general idea? ")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(0.5)


def showIdea():
  time.sleep(0.5)
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.readlines()  
  idea = random.choice(ideas).strip()
  f.close()
  print(f"Random idea from the list:\n{idea}\n")
  time.sleep(3)
  

main()