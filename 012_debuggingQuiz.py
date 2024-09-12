print("100 Days of Code QUIZ")

print()
print("How many can you answer correctly?")
score = 0

ans1 = input("What language are we writing in? ")
if ans1 == "python":
  print("Correct")
  score += 1
else:
  print("Nope🙈")
ans2 = int(input("Which lesson number is this? "))
if(ans2>12):
  print("We're not quite that far yet")
elif(ans2==12):
  print("That's right!")
  score += 1
else:
  print("We've gone well past that!")

print(f"Your score is {score}")