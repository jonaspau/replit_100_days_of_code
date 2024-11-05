from bs4 import BeautifulSoup
import requests

url = "https://www.nrk.no/"
response = requests.get(url)
response.encoding = response.apparent_encoding
html = response.text

soup = BeautifulSoup(html, "html.parser")

# Find all article containers
article_divs = soup.find_all("div", class_="kur-room-wrapper")

articles = {}

for article_div in article_divs:
    # Find the <a> tag in the article to get the URL
    a_tag = article_div.find("a")
    if a_tag and a_tag.get("href"):
        url = a_tag["href"]
        # Find the <h2> tag within the article to get the title
        h2_tag = article_div.find("h2", class_="kur-room__title")
        if h2_tag:
            title = h2_tag.get_text(strip=True)
            # Store the title and URL in the dictionary
            articles[title] = url

# print top 10 articles
n = 0
for title, url in articles.items():
  if n < 10:
    print(f"T: {title}")
    print(f"U: {url}\n")
    n +=1
  else:
    break
