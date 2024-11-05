# main.py
from re import template
from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/blog1")


@app.route('/blog1') 
def blog1():
    data = request.args
    theme = data.get("theme", "").lower()
    heading = "My First Blog Entry"
    date = "October 7, 2024"
    text = "Today I learned how to use Flask to create web apps. It was fun and insightful!"

    return render_page(theme, heading, date, text)


@app.route('/blog2')
def blog2():
    data = request.args
    theme = data.get("theme", "").lower()
    heading = "Another Post"
    date = "October 7, 2024"
    text = "Continuing the journey with Flask, today I delved deeper into routing."

    return render_page(theme, heading, date, text)


@app.route('/b1')
def b1():
    return redirect("/blog1")


@app.route('/b2')
def b2():
    return redirect("/blog2")


def render_page(theme, heading, date, text):
    css = 'styleLight.css' if theme == 'light' else 'style.css'
    
    with open("templates/blog.html", "r") as f:
        page = f.read()

    page = page.replace("{theme}", css)
    page = page.replace("{heading}", heading)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)

    return page


app.run(host='0.0.0.0', port=81)