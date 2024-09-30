from replit import db
from random import randint
import hashlib
import os
import time


def menu():
  print("--- Login menu ---\n")
  print("1: Create user")
  print("2: Login")
  option = input("Option: ")
  return(option)


def addUser():
  time.sleep(1)
  os.system("clear")
  
  print("--- Add user: ---\n")
  username = input("Username: ")
  password = input("Password: ")
  salt = randint(10000, 99999)
  
  keys = db.keys()
  if username in keys:
    print("Error, user exist already")
    return
  
  salted_pw = f"{password}{salt}"
  hashed_pw = hash_password(salted_pw)
  db[username] = {"password":hashed_pw, "salt": salt}
  print("Success, added User")
  return(True)


def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()


def login():
  time.sleep(1)
  os.system("clear")
  
  print("--- Login ---\n")
  username = input("Username: ")
  password = input("Password: ")
  
  keys = db.keys()
  if username not in keys:
    print("Error: Username or password incorrect")
    return
  
  salt = db[username]["salt"]
  salted_pw = f"{password}{salt}"
  hashed_pw = hash_password(salted_pw)

  if hashed_pw == db[username]["password"]:
    
    print("Login succsessful")
    
  else:
    print("Error: Username or password incorrect")
    return(False)
    
  return(True)

while True:
  option = menu()
  if option == "1":
    addUser()
  elif option == "2":
    login()
  else:
    break
    
  time.sleep(3)
  os.system("clear")
