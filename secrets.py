import os

password = os.environ["userpass"]
adminpass = os.environ["adminpass"]
username = os.environ["username"]
adminname = os.environ["adminname"]
user = input("Enter username: ")
userPass = input("Enter password: ")


if user == adminname and userPass == adminpass:
    print("Welcome my Lord!")
elif user == username and userPass == password:
    print("Welcome citizen.")
else:
  print("Unknown user or password!")
  print("Go away, peasant.")
