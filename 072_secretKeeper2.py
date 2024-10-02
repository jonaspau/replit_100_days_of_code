from replit import db
from random import randint
import os, datetime, hashlib


def main():
    if passwordCheck() == True:
        while True:
            head()
            print("What would you like to do? ")
            print("1: Tell a secret")
            print("2: See a secret")
            choice = input("Choice: ")
    
            if choice == "1":
                tellSecret()
            elif choice == "2":
                seeSecret()
            else:
                break
    else:
        head()
        print("Sorry wrong password!")
        exit()
    

def head():
    os.system("clear")
    print("--- My Secrets ---\n")


def tellSecret():
    head()
    secret = input("Tell me your secret (it is safe with me)\n\n")
    time = f"secr_{datetime.datetime.now()}"
    db[time] = secret


def seeSecret():
    keys = db.prefix("secr_")
    print(keys)
    for key in sorted(keys, reverse=True):
        head()
        print(db[key])
        more = input("\nWant me to tell you another secret y/n? ")
        if more == "n":
            break


def passwordCheck():
    head()
    keys = db.keys()
    
    if "password" not in keys:
        password = input("Set a password: ")
        salt = randint(10000, 99999)
        salted_pw = f"{password}{salt}"
        hashed_pw = hash_password(salted_pw)
        db["password"] = {"password":hashed_pw, "salt": salt}
        print("Created password")
        return(True)
    else:
        password = input("Password: ")
        salt = db["password"]["salt"]
        salted_pw = f"{password}{salt}"
        hashed_pw = hash_password(salted_pw)
        if hashed_pw == db["password"]["password"]:
            print("Login succsessful")
            return(True)
        else:
            return(False)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


main()
