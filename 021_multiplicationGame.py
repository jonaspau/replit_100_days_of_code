print("---Multiplication game---")

multiplier = int(input("Name your multiplier: "))
score = 0

for i in range(1, 11):
  print()
  answer = int(input(f"{i} x {multiplier} = "))
  if answer == i * multiplier:
    print("Great work!")
    score += 1
  else:
    print(f"Nope. The answer was {i * multiplier}")

print(f"You scored {score} out of 10.")