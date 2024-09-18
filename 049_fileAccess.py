f = open("high.score", "r")
highscore = 0
leader = ""

while True:
  content = f.readline().strip()
  if content == "":
    break
  initials, score = content.split()
  score = int(score)
  if score > highscore:
    highscore = score
    leader = initials

print(f"Winner: {leader}, with a score of {highscore}")

f.close()