from os import system
from time import sleep

tasks = []


def main():
  loadTasks()
  while True:
    print("--- To Do List ---\n")
    menu = input("1: Add\n2: View\n3: Remove\n4: Edit\n5: Exit\nOption: ")
    if menu == "1":
      add()
    elif menu == "2":
      view()
    elif menu == "3":
      remove()
    elif menu == "4":
      edit()
    elif menu == "5":
      saveTasks()
      break
    else:
      print("Invalid option")
      sleep(1)
    system("clear")
  saveTasks()


def loadTasks():
  global tasks
  f = open("051_tasks.txt", "r")
  tasks = eval(f.read())
  f.close()


def saveTasks():
  f = open("051_tasks.txt", "w")
  f.write(str(tasks))
  f.close()


def add():
  task = input("What is the task? ")
  due = input("When is it due? ")
  priority = input("What is the priority? ")
  row = [task, due, priority]
  tasks.append(row)
  print(f"Added {task} to the list")
  sleep(2)


def view():
  print("View")
  menu = input("1: View all\n2: View priority\nOption: ")
  if menu == "1":
    for row in tasks:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  elif menu == "2":
    priority = input("What priority? ")
    for row in tasks:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  else:
    print("Invalid option")
  sleep(2)


def remove():
  print("Remove")
  task = input("What task do you want to remove? ")
  for row in tasks:
    if task in row:
      tasks.remove(row)
      print(f"Removed {task} from the list")
      sleep(2)


def edit():
  print("Edit")
  task = input("What task do you want to edit? ")
  for row in tasks:
    if task in row:
      task = row[0]
      due = row[1]
      priority = row[2]
      print(f"T: {task} D: {due} P: {priority}")
      new_task = input("New task: ")
      new_due = input("New due: ")
      new_priority = input("New priority: ")
      row[0] = new_task
      row[1] = new_due
      row[2] = new_priority
      print(f"Edited {task} to {new_task}")
    sleep(2)


if __name__ == "__main__":
  main()
