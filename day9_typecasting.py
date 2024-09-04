# Make a generation calculator
# Generation Name	Starting Birth Year	Ending Birth Year
# Traditionalists	1925	1946
# Baby Boomers	1947	1964
# Generation X	1965	1981
# Millenials	1982	1995
# Generation Z	1996	2015

year_of_birth = int(input("What year were you born? "))

if year_of_birth >= 1925 and year_of_birth <= 1946:
  print("You are a Traditionalist")
elif 1947 <= year_of_birth <= 1964:
  print("You are a Baby Boomer")
elif 1965 <= year_of_birth <= 1981:
  print("You are a Generation X")
elif  1982 <= year_of_birth <= 1995:
  print("You are a Millenial")
elif 1996 <= year_of_birth <= 2015:
  print("You are a Generation Z")
else:
  print("You are either too old or too young to be on this list")
