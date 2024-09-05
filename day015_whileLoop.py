exit = ""

while exit != "y":
  print("What animal do you want to hear?")
  animal = input("Cow, Dog, Cat, or Frog? ").title()

  if animal == "Cow":
    print("A cow goes moo.")
  elif animal == "Dog":
    print("A dog goes woof.")
  elif animal == "Cat":
    print("A cat goes meow.")
  elif animal == "Frog":
    print("A frog goes ribbit.")
  else:
    print("I don't know that animal.")

  exit = input("Exit (y/n)? ").lower()