website = {
  "name": "",
  "url": "",
  "description": "",
  "rating": ""
}


for key in website.keys():
  website[key] = input(f"{key}: ")

os.system("clear")
print("--- Website info ---")
for key, value in website.items():
  print(f"{key}: {value}")