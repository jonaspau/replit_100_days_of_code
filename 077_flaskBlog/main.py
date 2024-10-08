# main.py
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/blog1')
def blog1():
    heading = "My First Blog Entry"
    date = "October 7, 2024"
    text = "Today I learned how to use Flask to create web apps. It was fun and insightful!"

    with open("template/blog.html", "r") as f:
        page = f.read()

    page = page.replace("{heading}", heading)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    return page

@app.route('/blog2')
def blog2():
    heading = "Another Post"
    date = "October 7, 2024"
    text = "Continuing the journey with Flask, today I delved deeper into routing."

    with open("template/blog.html", "r") as f:
        page = f.read()

    page = page.replace("{heading}", heading)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    return page

@app.route('/b1')
def b1():
    return redirect("/blog1")

@app.route('/b2')
def b2():
    return redirect("/blog2")

app.run(host='0.0.0.0', port=81)