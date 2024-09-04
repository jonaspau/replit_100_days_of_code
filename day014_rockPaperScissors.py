from getpass import getpass as input

choices = ["R", "P", "S"]
p1_hand = ""
p2_hand = ""

while p1_hand not in choices:
  p1_hand = input("Player 1, please enter your move (R, P, or S): ").upper()

while p2_hand not in choices:
  p2_hand = input("Player 2, please enter your move (R, P, or S): ").upper()

print(f"Player 1 played {p1_hand}")
print(f"Player 2 played {p2_hand}")

if p1_hand == p2_hand:
  print("It's a tie!")
else:
  if p1_hand == "R":
    if p2_hand == "S":
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")
  elif p1_hand == "P":
    if p2_hand == "R":
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")
  elif p1_hand == "S":
    if p2_hand == "P":
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")
      