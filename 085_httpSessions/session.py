from flask import Flask, request, redirect, session # extra session import
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionKey'] # new line to include the key, inside [''] is the key you created


@app.route('/')

def index():
  page = ""
  myName = ""
  if session.get("myName"):
    myName = session["myName"]
  page += f"<h1>{myName}</h1>"
  with open("form.html", "r") as f:
    page += f.read()
  return page

@app.route("/setName", methods=["POST"])
def setName():
  session["myName"] = request.form["name"]
  return redirect("/")

@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port=81)