import requests, sys, os, time
from replit import db

def main():
  while True:
    choice, joke = showMenu()
    if choice == "s":
      db[joke] = joke
    elif choice == "l":
      loadJokes()
    elif choice == "n":
      continue
    elif choice =="q":
      sys.exit()
    elif choice == "d":
      deleteJokes()
    

# Function to display the menu with a random joke and get user's choice
def showMenu():
  os.system("clear")
  joke = showRandomJoke()
  choice = ""
  print("(s)ave, (l)oad old, (n)ew joke, (q)uit")
  # Loop until a valid choice is made
  while True:
    choice = input("> ").strip().lower()
    if choice in ("s", "l", "n", "q", "d"):
      return choice, joke
    else:
      print("\033[F", end="")


# Function to fetch and print a random joke from the API
def showRandomJoke():
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  joke = result.json()
  print(joke["joke"])
  return joke["id"]


# Display all saved jokes from the database
def loadJokes():
  os.system("clear")
  keys = db.keys()

  for key in keys:
    result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept":"application/json"})
    joke = result.json()
    print(joke["joke"])
    time.sleep(3)


# Hidden function to delete all jokes from the database
def deleteJokes():
  keys = db.keys()
  for key in keys:
    del db[key]

main()
