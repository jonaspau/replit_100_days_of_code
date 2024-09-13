 os
import time

mokeDex = {
  "Beast Name": "",
  "Type": "",
  "Special Move": "",
  "HP": "",
  "MP": "",
}

def main():
  getBeast()
  printBeast()

def getBeast():
  print("--- Add to MokeDex ---\n")
  for name, value in mokeDex.items():
    mokeDex[name] = input(f"{name}: ").strip().title()
  time.sleep(0.2)
  os.system("clear")

def printBeast():
  print("--- MokeDex ---\n")
  for name, value in mokeDex.items():
      if mokeDex["Type"] == "Fire":
        print("\033[31m", end="")
      elif mokeDex["Type"] == "Water":
        print("\033[34m", end="")
      elif mokeDex["Type"] == "Air":
        print("\033[37m", end="")
      elif mokeDex["Type"] == "Earth":
        print("\033[32m", end="")
      elif mokeDex["Type"] == "Spirit":
        print("\033[35m", end="")
      print(f"{name:<15}: {value}")

main()