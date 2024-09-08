print("30 days of code. What did you think?\n")
for i in range (30):
  answer = input(f"Day {i+1}\n")
  print()
  response = f"You thought day {i+1} was {answer} \n"
  print(f"{response: ^36}")
