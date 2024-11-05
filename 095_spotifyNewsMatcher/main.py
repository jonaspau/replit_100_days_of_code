import requests, json, os
from requests.auth import HTTPBasicAuth
from openai import OpenAI


def main():
  print("--- Welcome ---")
  news = getNews()
  spotifyToken = spotifyAuthenticate()

  for title in news:
    newTitle = shorten(title)
    print(title)
    print(newTitle)
    search = newTitle.replace(" ", "%20")
    print(spotifySearch(spotifyToken, search))
    print()


def shorten(title):
  client = OpenAI(api_key=os.environ['OPENAI'])

  prompt = f"Write this title in 2-4words: {title}"

  response = client.chat.completions.create(model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content":f"{prompt}"}
  ],
  max_tokens=40,
  temperature=0)
  return response.choices[0].message.content.strip()

def getNews():
  newsAPIkey = os.environ['NEWS_API']

  url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPIkey}"
  response = requests.get(url)
  response = response.json()
  # print(json.dumps(response, indent=2))

  news = []
  for article in response["articles"]:
    if len(news) < 5:
      title = (article["title"])
      news.append(title)
    else:
      break

  return news
    
def spotifyAuthenticate():
  client = os.environ['SPOTIFY_ID']
  secret = os.environ['SPOTIFY_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type": "client_credentials"}
  auth = HTTPBasicAuth(client, secret)

  response = requests.post(url, data=data, auth=auth)
  token = response.json()["access_token"]
  return token


def spotifySearch(token, search):
  url = "https://api.spotify.com/v1/search"
  headers = {"Authorization": f"Bearer {token}"}
  search = f"?q={search}&type=track&limit=1&offset=0"
  
  url = f"{url}{search}"

  response = requests.get(url, headers=headers)
  data = response.json()

  tracks = data.get("tracks", {}).get("items", [])
  if tracks:
    track = tracks[0]
    preview_url = track.get("preview_url")
    return preview_url
  else:
    return "No preview available"

if __name__ == "__main__":
  main()