import os
import time
import random

tasks = []
file = "055_tasks.txt"
backup_folder = "backup"


def main():
  loadTasks()
  while True:
    print("--- To Do List ---\n")
    menu = input("1: Add\n2: View\n3: Remove\n4: Edit\nq: Exit\nOption: ")
    if menu == "1":
      add()
    elif menu == "2":
      view()
    elif menu == "3":
      remove()
    elif menu == "4":
      edit()
    elif menu == "q":
      saveTasks()
      break
    else:
      print("Invalid option")
      time.sleep(1)
    os.system("clear")


def loadTasks():
  global tasks, file

  files = os.listdir()
  if file not in files:
    tasks = []
  else:
    f = open(file, "r")
    tasks = eval(f.read())
    f.close()


def saveTasks():
  global file, backup_folder, tasks
  files = os.listdir()
  if backup_folder not in files:
    os.mkdir(backup_folder)
  os.rename(file, backup_folder + "/" + str(random.randint(10000, 99999)) + file)
  f = open(file, "w")
  f.write(str(tasks))
  f.close()


def add():
  task = input("What is the task? ")
  due = input("When is it due? ")
  priority = input("What is the priority? ")
  row = [task, due, priority]
  tasks.append(row)
  saveTasks()
  print(f"Added {task} to the list")
  time.sleep(2)


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
  time.sleep(2)


def remove():
  print("Remove")
  task = input("What task do you want to remove? ")
  for row in tasks:
    if task in row:
      tasks.remove(row)
      saveTasks()
      print(f"Removed {task} from the list")
      time.sleep(2)


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
    time.sleep(2)


if __name__ == "__main__":
  main()
