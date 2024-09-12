username = input("Enter your name: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin":
  print(f"Hello {username}, what do you want to mess up today?")
elif username == "Jonas" and password == "godmode":
  print(f"Hello {username}, you have unlocked godmode!")
elif username == "user" and password == "user":
  print(f"Hello {username}, what do you want to do today?")
else:
  print("I'm sorry, but you are not allowed to use this program.")