amount = 1000
years = 10
pct = 0.05

for i in range(10):
  amount += amount * pct
  print(f"Owed in year {i+1}: ${round(amount, 2)}")