likes_python = input("Do you like Python? ")

if likes_python == "yes":
  print("Yay!")
  portfolio = input("Do you have a portfolio? ")
  if portfolio == "yes":
    print("Great!")
    github = input("Do you have a github account? ")
    if github == "yes":
      print("Awesome!")
      stores_on_gh = input("Do you sync your files to github? ")
      if stores_on_gh == "yes":
        print("Good")
        uses_ui = input("Do you use a UI to sync your files or the terminal? ")
        if uses_ui == "ui":
          print("You are no friend of mine!")
        else:
          print("You are my friend!")
      else:
        print("You should sync your files to github")
    else:
      print("You should make one!")
  else:
    print("Get one!")
else:
  print("Oh no!")