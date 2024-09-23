from replit import db
import datetime
import os
import time


def addTweet():
    message = input("Enter your message: ").strip().capitalize()
    timestr = f"msg_{datetime.datetime.now()}"
    db[timestr] = message
    time.sleep(2)
    os.system("clear")


def viewTweets():
    keys = db.prefix("msg_")
    count = 0
    for key in sorted(keys, reverse=True):
        print(f"{key}: {db[key]}")
        count += 1
        if count == 10:
            more = input("Show more y/n? ")
            if more == "n":
                os.system("clear")
                menu()
            else:
                count = 0
                os.system("clear")
    time.sleep(5)
    os.system("clear")


def menu():
    print("--- The BirdApp ---\n")
    menu = input("1: Add tweet\n2: View Tweets\n\nOption: ")
    if menu == "1":
        addTweet()
    elif menu == "2":
        viewTweets()
    else:
        print("Goodbye")
        time.sleep(2)
        os.system("clear")
        return False


while True:
    if menu() is False:
        break
    else:
        menu()
