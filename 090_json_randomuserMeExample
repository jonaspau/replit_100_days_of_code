import json
import requests

for _ in range(10):
  # Send a GET request to fetch user data from the Random User API
  results = requests.get("https://randomuser.me/api/")
  # Parse the JSON response
  user = results.json()

  # Construct the filename using the user's first and last name
  name = f"{user['results'][0]['name']['first']}_{user['results'][0]['name']['last']}"
  filename = f"images/{name}.jpg"

  # Extract the URL of the user's medium-sized picture
  image_url = f"{user['results'][0]['picture']['medium']}"
  # Send a GET request to fetch the image
  image = requests.get(image_url)
  
  # Open a file and store the image
  f = open(filename, "wb")
  f.write(image.content)
  f.close()
