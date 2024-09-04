print("""Welcome to your adventure simulator. 
I am going to ask you a bunch of questions and then create an epic story with you as the star!
""")

name = input("What is your name? ")
enemy = input("What is your worst enemy’s name? ")
superpower = input("What is your superpower? ")
place = input("Where do you live? ")
food = input("What is your favorite food? ")

print()
print(f"""Hello {name}! 
Your ability to {superpower} will make sure you never have to look at \033[31m{enemy}\033[0m again. 
Go eat {food} as you walk down the streets of {place} and use {superpower} for good and not evil!"""
      )
