import schedule, time, smtplib, os, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
  quotes = getQuotes()
  
  schedule.every(1).days.do(sendQuote, quotes)
  while True:
    schedule.run_pending()
    time.sleep(1)

def sendQuote():
  quote = getQuote(quotes)
  sendMail(quote)


def sendMail(text):
  gmail_user = os.environ['gmail_user']
  gmail_pass = os.environ['gmail_pass']

  email = f"{text}"
  server = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(gmail_user, gmail_pass)

  msg = MIMEMultipart()
  msg["To"] = "jonas.paulsen@nav.no"
  msg["From"] = gmail_user
  msg["Subject"] = "Quote of the day!"
  msg.attach(MIMEText(email, "html"))

  s.send_message(msg)
  del msg


def getQuotes():
  quotes = []
  with open("motivational_quotes.txt", "r") as f:
    for line in f:
      parts = line.split(". ", 1)
      if len(parts) == 2:
        quote = parts[1].strip()
        quotes.append(quote)
  return quotes


def getQuote(quotes):
  n_quotes = len(quotes) - 1
  quote_id = random.randint(0,n_quotes)
  quote = quotes[quote_id]
  return quote


if __name__ == "__main__":
  main()