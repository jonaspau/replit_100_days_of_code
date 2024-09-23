from replit import db
import os, datetime

keys = db.keys()


def main():
    passwordCheck()

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
    userpw = input("Enter password: ")
    if "password" in keys:
        dbpw = db["password"]
        if userpw != dbpw:
            print("Incorrect")
            os._exit(0)
        else:
            os.system("clear")
    else:
        db["password"] = userpw


main()
