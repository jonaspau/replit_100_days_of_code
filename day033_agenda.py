from os import system
from time import sleep


myAgenda = []

def printAgenda():
  print("--- My Agenda ---\n")
  for item in myAgenda:
    print(item)

printAgenda()

while True:
  menu = input("\nAdd (A), Remove (R) or Edit (E)?: ").upper()
  if menu == "A":
    item = input("What's next on the agenda? ")
    myAgenda.append(item)
  
  elif menu == "R":
    item = input("What do you want to remove? ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
    sleep(1)
  
  elif menu == "E":
    item = input("What do you want to edit? ")
    new = input("What do you want to change it to? ")
    for i in range(0, len(myAgenda)):
      if item in myAgenda:
        myAgenda[i] = new
  
  else:
    print("Invalid input")
    sleep(1)
  
  system("clear")
  printAgenda()
