import requests, json, os
from requests.auth import HTTPBasicAuth


def main():
  token = authenticate()

  year = input("Year: ")
  result = search(token, year)


def authenticate():
  client = os.environ['CLIENT_ID']
  secret = os.environ['CLIENT_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type": "client_credentials"}
  auth = HTTPBasicAuth(client, secret)

  response = requests.post(url, data=data, auth=auth)
  token = response.json()["access_token"]
  return token


def search(token, year):
  url = "https://api.spotify.com/v1/search"
  headers = {"Authorization": f"Bearer {token}"}
  search = f"?q=year%3A{year}&type=track&limit=10"

  url = f"{url}{search}"

  response = requests.get(url, headers=headers)
  data = response.json()

  tracks = []
  for track in data["tracks"]["items"]:
      track_info = {
          "name": track["name"],
          "artist": track["artists"][0]["name"],
          "preview_url": track["preview_url"],
          "release_date": track["album"]["release_date"]
      }
      tracks.append(track_info)

  return tracks


if __name__ == "__main__":
  main()