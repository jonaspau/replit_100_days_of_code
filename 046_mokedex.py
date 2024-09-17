import os


mokedex = {}


def main():
  getBeast()
  printMokedex()
  

def printMokedex():
  print(f"Name\tType\tHP\tMP")
  for beast, stats in mokedex.items():
    print(f"name: {beast}", end=" | ")
    for stat, value in stats.items():
      print(f"{stat}: {value}", end=" | ")
    print()


def getBeast():
  while True:
    print("--- Add to MokeDex ---\n")
    name = input("Enter the beast name: ")
    element = input("Enter the element: ")
    special_move = input("Special move: ")
    starting_hp = input("Starting HP: ")
    starting_mp = input("Starting MP: ")
  
    mokedex[name] = {
      "element": element,
      "special move": special_move,
      "HP": starting_hp,
      "MP": starting_mp
    }
    

    again = input("\nAdd another (y/n)? ").lower()
    if again == "n":
      os.system("clear")
      break      
    os.system("clear")


main()