import os


f = open("high.score", "a+")

while True:
  initials = input("Initials: ")
  score = int(input("Score: "))
  
  f.write(f"{initials} {score}\n")
  print(f"Added {initials} {score}")

  again = input("Add another (y/n)? ")
  if  again == "n":
    f.close()
    break
  os.system("clear")