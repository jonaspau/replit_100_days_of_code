from bs4 import BeautifulSoup
import requests, json, os
from openai import OpenAI

def main():
  text, refs = getArticle()
  summary = summarize(text)
  print(summary)

  for ref in refs:
    print(ref)

def getArticle():
  url =  "https://en.wikipedia.org/wiki/Python_(programming_language)"
  
  response = requests.get(url)
  response.encoding = response.apparent_encoding
  html = response.text
  
  soup = BeautifulSoup(html, "html.parser")
  
  text = ""
  
  article = soup.find_all("div", {"class": "mw-parser-output"})
  
  for articles in article:
    content = articles.find_all("p")  
    for p in content:
      text += p.text

  refs = soup.find_all("ol", {"class": "references"})
  hrefs = []
  for ref in refs:
    hrefs.append(ref.text.replace("^ ",""))
    


  return text, hrefs

def summarize(text):
  client = OpenAI(api_key=os.environ['OPENAI'])

  prompt = f"Summarize this text in three paragraphs: {text}"

  response = client.chat.completions.create(model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content":f"{prompt}"}
  ],
  max_tokens=300,
  temperature=0)
  return response.choices[0].message.content.strip()
  
if __name__ == "__main__":
  main()