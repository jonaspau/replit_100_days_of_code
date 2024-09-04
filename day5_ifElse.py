# Character guesstimator

super_strength = input("Does your character have super strength? (y/n) ")
if super_strength.lower() == "n":
  rough_voice = input("Does your character have a rough voice? (y/n) ")
  
  if rough_voice.lower() == "n":
    print("Are you just a regular Joe?")
  else:
    print("You're Batman!")

else:
  spiders = input("Does your character like spiders? (y/n) ")
  
  if spiders.lower() == "y":
    print("Are you spiderman?")
  else:
    print("Never heard of you.")
