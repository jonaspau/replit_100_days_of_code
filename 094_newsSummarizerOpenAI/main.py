import requests, json, os
from openai import OpenAI

def main():
  news = getNews()
  
  for title in news:
    newTitle = enrich(title)
    print(title)
    print(newTitle)
    print()
  
def enrich(title):
  client = OpenAI(api_key=os.environ['OPENAI'])
  
  prompt = f"Write this title in a funnier way: {title}"
  
  response = client.chat.completions.create(model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content":f"{prompt}"}
  ],
  max_tokens=40,
  temperature=0)
  return response.choices[0].message.content.strip()


def getNews():
  newsAPIkey = os.environ['NEWS_API_KEY']
  
  url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPIkey}"
  response = requests.get(url)
  response = response.json()
  # print(json.dumps(response, indent=2))

  news = []
  for article in response["articles"]:
    title = (article["title"])
    news.append(title)

  return news

if __name__ == "__main__":
  main()