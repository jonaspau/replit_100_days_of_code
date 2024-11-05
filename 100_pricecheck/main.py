# main.py

from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
from threading import Thread
import requests, smtplib, os, schedule, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

def scheduled_task():
    products = read_products_file()
    scrape_product_price(products)

def run_scheduled_task():
    schedule.every(12).hours.do(scheduled_task)

    while True:
        schedule.run_pending()
        time.sleep(60)

def start_scheduler():
    scheduler_thread = Thread(target=run_scheduled_task)
    scheduler_thread.start()
    print("Started email scheduler for 12 hours")

def extract_price_from_url(url):
    try:
        # Fetch the HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the <meta> tag with property="og:amount"
        price_meta = soup.find('meta', property='og:amount')

        if price_meta and price_meta.has_attr('content'):
            # Extract the price content
            current_price = price_meta['content']
            return current_price
    except requests.RequestException as e:
        print(f"Error retrieving the price from {url}: {e}")
        return "N/A"

def scrape_product_price(products):
    for product in products:
        product['current_price'] = extract_price_from_url(product['url'])

        try:
            current_price = float(product["current_price"])
            price_warning = float(product["price_warning"])

            if current_price < price_warning:
                subject = f"Price alert for {product['name']}"
                body = f"""The current price for {product['name']} is {current_price}.
                Which is lower than your price alert {price_warning}"""
                send_email(subject, body)
        except ValueError:
            print(f"Failed to evaluate price for {product['name']}")

def read_products_file():
    products = []
    with open("products.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            name, url, price_warning = line.strip().split(', ')
            products.append({
                'name': name,
                'url': url,
                'price_warning': price_warning
            })
    return products

def send_email(subject, body):
    gmail_user = os.environ['gmail_user']
    gmail_pass = os.environ['gmail_pass']
    recipient = os.environ["email_recipient"]

    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(gmail_user, gmail_pass)
    
    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    s.send_message(msg)
    s.quit()

    
@app.route("/")
def home():
    products = read_products_file()
    scrape_product_price(products)  # Fetch and update current prices for each product
    return render_template('index.html', products=products)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    url = request.form.get("url")
    price_warning = request.form.get("price_warning")

    data = f"{name}, {url}, {price_warning}\n"

    with open("products.txt", "a") as f:
        f.write(f"{data}")

    return redirect("/")

if __name__ == '__main__':
    start_scheduler()
    app.run(host="0.0.0.0", port=81)