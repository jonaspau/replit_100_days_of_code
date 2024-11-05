import datetime
from flask import Flask, request, redirect
from replit import db

app = Flask(__name__)

def getChat():
  message = ""
  f = open("message.html", "r")
  message = f.read()
  f.close()
  
  keys = db.keys()
  keys = list(keys)
  result = ""
  recent = 0

  for key in reversed(keys):
    myMessage = message
    myMessage = myMessage.replace("{username}", db[key]["username"])
    myMessage = myMessage.replace("{timestamp}", key)
    myMessage = myMessage.replace("{message}", db[key]["message"])
    username = request.headers["X-Replit-User-Name"]
    if username == "jonaspau":
      myMessage = myMessage.replace("{admin}", f""" <a href="/delete?id={key}">Delete message</a>""")
    else:
      myMessage = myMessage.replace("{admin}", "")
    
    result += myMessage
    recent +=1
    if recent == 5:
      break
  return result

    
@app.route("/")
def index():
  page = ""
  f = open("chat.html", "r")
  page = f.read()
  f.close()

  username = request.headers.get("X-Replit-User-Name")
  page = page.replace("{username}", username)
  page = page.replace("{chats}", getChat())
  return page


@app.route("/add", methods=["POST"])
def add():
  form = request.form
  message = form["msg"]
  date = datetime.datetime.now()
  timestamp = datetime.datetime.timestamp(date)
  userid = request.headers["X-Replit-User-Id"]
  username = request.headers["X-Replit-User-Name"]
  db[timestamp] = {"userid": userid, "username": username, "message": message}
  return redirect("/")


@app.route("/delete", methods=["GET"])
def delete():
  username = request.headers["X-Replit-User-Name"]
  if username != "jonaspau":
    return redirect("/")

  results = request.values["id"]
  del db[results]
  return redirect("/")
  

@app.route("/logout", methods=["POST"])
def logout():
    response = redirect("/")
    return response

app.run(host="0.0.0.0", port=81)