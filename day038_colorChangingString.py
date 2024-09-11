def colorChanger(color):
  for letter in myString:
    if letter.lower() == "r":
      print("\033[31m", letter, sep="", end="")
    elif letter.lower() == "g":
      print("\033[32m", letter, sep="", end="")
    elif letter.lower() == "y":
      print("\033[33m", letter, sep="", end="")
    elif letter.lower() == "b":
      print("\033[34m", letter, sep="", end="")
    elif letter.lower() == "p":
      print("\033[35m", letter, sep="", end="")
    elif letter == " ":
      print("\033[0m", letter, sep="", end="")
    else:
      print(letter, end="")

myString = input("Enter a string: ")
colorChanger(myString)