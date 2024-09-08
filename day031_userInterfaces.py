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


print("          ", end="")
customprint("=", "red")
customprint("=", "white")
customprint("=", "blue")
customprint(" Music App ", "yellow")
customprint("=", "blue")
customprint("=", "white")
customprint("=", "red")
print("\n")
print("🔥▶️","   Radio Gaga")
print("       Queen")
print("\n")
print("PREV")
customprint("       NEXT\n", "green")
customprint("              PAUSE", "purple")


title = "WELCOME TO"
title2 = "--    ARMBOOK    --\n"
text = "Definitely not a rip off of\n"
text2 = "a certain other social\n"
text3 = "networking site.\n"
text4 = "Honest."
username = "Username:"
password = "Password:"

print("\n\n\n")
print(f"{title:^35}")
customprint(f"{title2:^35}", "blue")
customprint(f"{text:>25}", "yellow")
customprint(f"{text2:>35}", "yellow")
customprint(f"{text3:>35}", "yellow")
print()
customprint(f"{text4: >20}", "red")
print("\n")
print(f"{username:^33}")
print(f"{password:^33}")
