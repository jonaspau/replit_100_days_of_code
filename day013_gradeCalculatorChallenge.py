print("--- Grade Calculator ---")

# Get user input
subject = input("Enter the subject: ")
score = int(input("Enter the score: "))
possible_score = int(input("Enter the possible score: "))
print()

# Calculate percentage
pct = round(score / possible_score * 100)
print(f"You got {pct}% in {subject}.")
print()

# Convert to grade
if pct >= 90:
  print(f"Congratulations. {pct}% means you got an A+.")
  print("🍾🎂🎁")
elif pct >= 80:
  print(f"Congratulations. {pct}% means you got an A.")
  print("🍾🎂")
elif pct >= 70:
  print(f"Well done, {pct}% means you got a B.")
  print("🥐")
elif pct >= 60:
  print(f"{pct}% means you got a C.")
  print("🍪")
elif pct >= 50:
  print(f"{pct}% means you got a D.")
  print("😬")
elif pct >= 40:
  print(f"{pct}% means you got ungraded.")
  print("Time to hit those books.")
