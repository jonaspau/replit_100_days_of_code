solution = 854325
answer = 0
attempts = 0

while True:
  answer = int(input("Guess a number between 1 and 1 000 000: "))
  if answer != solution:
    if answer > solution:
      print("Too high")
      attempts += 1
      continue
    elif answer < solution:
      print("Too low")
      attempts += 1
      continue
  else:
    attempts += 1
    print(f"You guessed it in {attempts} attempts!")
    print("Thanks for playing. Goodbye...")
    break