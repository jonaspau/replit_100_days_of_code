from os import system
from time import sleep


myAgenda = []

def printAgenda():
  print("--- My Agenda ---\n")
  for item in myAgenda:
    print(item)
    
print("--- My Agenda ---\n")
while True:
  menu = input("\nAdd (A) or Remove (R)?: ")
  if menu == "A":
    item = input("What's next on the agenda? ")
    myAgenda.append(item)
    system("clear")

  elif menu == "R":
    item = input("What do you want to remove? ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
    sleep(1)
    system("clear")

  else:
    print("Invalid input")
    sleep(1)
    system("clear")
  printAgenda()
