def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value - 1)

result = factorial(500)
print(result)
