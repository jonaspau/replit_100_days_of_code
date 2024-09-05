attempts = 0

while True:
  print("----------------")
  print("Guess the lyrics")
  print()
  print("Finnes det en _____, slik som jeg vil ha.")
  print("What is the missing word?")
  answer = input("Your answer: ")
  attempts += 1
  print()
  
  if answer == "kvinne":
    print("Correct!")  
    break
  

if attempts == 1:
  print("Lyrics-master! You got it on your first try!")
else:
  print("You got the correct word in", attempts, "attempts.")