from os import system
from time import sleep

myAgenda = []


def printHead():
  print("--- My Agenda ---\n")


def printAgenda():
  printHead()
  for index in range(len(myAgenda)):
    print(f"{index}: {myAgenda[index]}")
  print()


def printItem(item):
  system("clear")
  printHead()
  print(f"\n{myAgenda[item]}")
  sleep(3)

def printMenu():
  return(input("1: Add\n2: View\n3: Remove\n4: Edit\n0: Quit\nOption: ").upper())


while True:
  printAgenda()
  menu = printMenu()
  if menu == "1":
    item = input("What's next on the agenda? ")
    myAgenda.append(item)

  elif menu == "2":
    index = int(input("Which item do you want to view? "))
    if 0 <= index <= len(myAgenda):
      printItem(index)

  elif menu == "3":
    index = int(input("What do you want to remove? "))
    if 0 <= index <= len(myAgenda):
      del myAgenda[index]

  elif menu == "4":
    index = int(input("What do you want to edit? "))
    new = input("What do you want to change it to? ")
    myAgenda[index] = new

  elif menu == "0":
    break

  else:
    print("Invalid input")
    sleep(1)

  system("clear")
