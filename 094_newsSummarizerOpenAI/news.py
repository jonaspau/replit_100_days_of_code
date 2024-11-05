
newsAPIkey = os.environ['NEWS_API_KEY']

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPIkey}"
response = requests.get(url)
response = response.json()
# print(json.dumps(response, indent=2))

for article in response["articles"]:
  title = (article["title"])

