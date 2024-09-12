import os
import time

contactCard = {
  "name": "",
  "dob": "",
  "phone": "",
  "email": "",
  "address": ""
}


def main():
  getInput()
  printContactCard()

  
def getInput(): 
  contactCard["name"] = input("Input your name : ").strip().title()
  contactCard["dob"] = input("Input your date of birth : ").strip()
  contactCard["phone"] = input("Input your phone number : ").strip()
  contactCard["email"] = input("Input your email : ").strip().lower()
  contactCard["address"] = input("Input your address : ").strip().title()
  time.sleep(0.5)
  os.system("clear")


def printContactCard():
  print("--- Contact information ---")
  print(f"Name: {contactCard['name']}")
  print(f"Date of birth: {contactCard['dob']}")
  print(f"Phone: {contactCard['phone']}")
  print(f"Email: {contactCard['email']}")
  print(f"Address: {contactCard['address']}")


if __name__ == "__main__":
  main()