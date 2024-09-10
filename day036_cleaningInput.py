people = []

def printPeople():
  print()
  for name in people:
    print(name)
  print()

while True:
  firstName = input("Enter your first name: ").strip().capitalize()
  lastName = input("Enter your last name: ").strip().capitalize()
  fullName = (f"{firstName} {lastName}")
  
  if fullName not in people:
    people.append(fullName)
  else:
    print(f"{fullName} is already in the list.")
  printPeople()