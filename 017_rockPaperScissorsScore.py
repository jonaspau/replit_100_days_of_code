from getpass import getpass as input

choices = ["R", "P", "S"]

p1_score = 0
p2_score = 0

while True:
  p1_hand = ""
  p2_hand = ""
  
  while p1_hand not in choices:
    p1_hand = input("Player 1, please enter your move (R, P, or S): ").upper()
  
  while p2_hand not in choices:
    p2_hand = input("Player 2, please enter your move (R, P, or S): ").upper()
  print()

  
  print(f"Player 1 played {p1_hand}")
  print(f"Player 2 played {p2_hand}")
  print()
  
  if p1_hand == p2_hand:
    print("It's a tie!")
  else:
    if p1_hand == "R":
      if p2_hand == "S":
        print("Rock beats scissors!")
        p1_score += 1
      else:
        print("Paper beats rock!")
        p2_score += 1
    elif p1_hand == "P":
      if p2_hand == "R":
        print("Paper beats rock!")
        p1_score += 1
      else:
        print("Scissors beats paper!")
        p2_score += 1
    elif p1_hand == "S":
      if p2_hand == "P":
        print("Scissors beats paper!")
        p1_score += 1
      else:
        print(f"Rock beats scissors!")
        p2_score += 1
        
  print(f"Player 1 score: {p1_score}, Player 2 score: {p2_score}")
  
  if p1_score == 3 or p2_score == 3:
    if p1_score > p2_score:
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")  
    print("Thanks for playing!")
    break
  else:
    continue

