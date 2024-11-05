"""
This script fetches the latest programming articles from Wired's programming section
and sends an email notification with new headlines that contain specific keywords.

Usage:
- Ensure you have set the necessary environment variables for Gmail authentication: 
  'gmail_user' and 'gmail_pass'.
- Run this script, and it will execute the `getNews()` function immediately and then
  every 6 hours thereafter.
- The email recipients and sender are defined within the script and should be adjusted
  for your needs.
"""

import schedule, time, smtplib, os, requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup 

def fetch_headlines():
    # Fetch latest articles from Wired's programming section
    url = "https://www.wired.com/tag/programming/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all articles with the given class and extract headline and link
    articles = soup.find_all("a", class_="SummaryItemHedLink-civMjp")
    return [(article.find('h3').text.strip(), "https://www.wired.com" + article['href']) for article in articles if article.find('h3')]

def filter_headlines(headlines):
    # Define keywords to look for in headlines
    keywords = [
        "python",
        "javascript",
        "html",
        "css",
        "react",
        "node.js",
        "django",
        "flask",
        "apis",
        "sql",
        "git",
        "devops"
    ]

    # Filter headlines that contain any of the keywords
    filtered_headlines = [
        (heading, link) for heading, link in headlines
        if any(keyword.lower() in heading.lower() for keyword in keywords)
    ]
    return filtered_headlines

def load_existing_headlines(filename='sent.txt'):
    try:
        with open(filename, 'r') as f:
            return set(tuple(line.strip().split(', ', 1)) for line in f if line.strip())
    except FileNotFoundError:
        return set()

def archive_new_headlines(new_headlines, filename='sent.txt'):
    with open(filename, 'a') as f:
        for heading, link in new_headlines:
            f.write(f"{heading}, {link}\n")

def sendEmail(headlines):
    gmail_user = os.environ['gmail_user']
    gmail_pass = os.environ['gmail_pass']
    email_recipient = os.environ['email_recipient']

    # Construct HTML email content
    email = "<html><body><h2>New Articles:</h2><ul>"
    for heading, link in headlines:
        email += f'<li><a href="{link}">{heading}</a></li>'
    email += "</ul></body></html>"

    # Set up SMTP connection
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(gmail_user, gmail_pass)

    # Create email message
    msg = MIMEMultipart()
    msg["To"] = email_recipient
    msg["From"] = gmail_user
    msg["Subject"] = "New programming articles!"
    msg.attach(MIMEText(email, "html"))

    # Send the email
    s.send_message(msg)
    s.quit()

def getNews():
    # Load current set of sent headlines
    existing_headlines = load_existing_headlines()

    # Fetch and filter headlines
    fetched_headlines = fetch_headlines()
    relevant_headlines = filter_headlines(fetched_headlines)

    # Identify new headlines that haven't been sent
    new_headlines = [
        (heading, link) for heading, link in relevant_headlines
        if (heading, link) not in existing_headlines
    ]

    # If there are new headlines, archive and send them
    if new_headlines:
        archive_new_headlines(new_headlines)
        sendEmail(new_headlines)
        print("Sent new links")

def main():
    # Call getNews immediately and schedule it to run every 6 hours
    getNews()
    schedule.every(6).hours.do(getNews)

    # Continuously check for scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()