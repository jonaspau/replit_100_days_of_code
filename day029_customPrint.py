def customprint(text, color):
  if color == "black":
    print(text, "\033[0;30m", end="")
  elif color == "red":
    print("\033[0;31m" + text + "\033[0m", sep="", end="")
  elif color == "green":
    print("\033[0;32m" + text + "\033[0m", sep="", end="")
  elif color == "brown":
    print("\033[0;33m" + text + "\033[0m", sep="", end="")
  elif color == "blue":
    print("\033[0;34m" + text + "\033[0m", sep="", end="")
  elif color == "purple":
    print("\033[0;35m" + text + "\033[0m", sep="", end="")
  elif color == "cyan":
    print("\033[0;36m" + text + "\033[0m", sep="", end="")
  elif color == "yellow":
    print("\033[1;33m" + text + "\033[0m", sep="", end="")
  else:
    print("\033[0m" + text + "\033[0m", sep="", end="")

customprint("Super Subroutine\n\n" , "")
customprint("With my ", "")
customprint("new program ", "blue")
customprint("I can just call ", "green")
customprint("red ", "red")
customprint("and that word will appear in the color I set it to.\n\n", "yellow")
customprint("awesome", "purple")
