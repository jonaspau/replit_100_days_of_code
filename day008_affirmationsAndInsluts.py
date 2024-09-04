# Get some input to play with
username = input("What is your name: ")
day_of_week = input("What day of the week is it: ")
favorite_things = input("What are your favorite things to do? ")
boring_dinner = input("What@s a boring thing to have for dinner?")

# Fix casing of variables
username = username.title()
day_of_week = day_of_week.title()
favorite_things = favorite_things.lower()
boring_dinner = boring_dinner.lower()

# Print out the message
if username in (Jonas, Admin, God, User):
  if day_of_week == "Monday":
    print(
        f"Hello {username}, sucks to be you it's Monday and a full week of work ahead! Guess you'd rather be {favorite_things}"
    )
  elif day_of_week == "Tuesday":
    print(
        f"Hello {username}, it's Tuesday and you're still working hard! Four more days before {favorite_things}"
    )
  elif day_of_week in ("Wednesday", "Thursday"):
    print(
        f"Hello {username}, it's {day_of_week} and you're still working hard, almost done with a pointless week! left-over {boring_dinner} for dinner today"
    )
  elif day_of_week == "Friday":
    print(
        f"Hello {username}, it's Friday and you're done with the week! You can rest now, {favorite_things} is your favorite thing to do"
    )
  elif day_of_week == "Saturday":
    print(
        f"Hello {username}, it's Saturday and you're done with the week! You can rest now"
    )
  elif day_of_week == "Sunday":
    print(
        f"Haha, wasted the entire weekend {favorite_things}. Guess you're looking forward to a full work week at the office. Good luck!"
    )
else:
  print("I don't know you, i suggest you fuck off")