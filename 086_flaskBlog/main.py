import os
from flask import Flask, request, render_template, session
from replit import db
from werkzeug.utils import redirect


app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ['sessionKey']

def read_template(file_name):
  with open(f"templates/{file_name}", "r") as file:
      return file.read()


@app.route('/')
def index():
  if "username" in session:
    user = session["username"]
    name = db.get(user,{}).get("name", "User")
    return render_template("welcome.html", name=name)
  else:
    return render_template("index.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect('/')
    user = session['username']
    name = db.get(user, {}).get('name', 'User')
    return render_template("welcome.html", name=name)
  
@app.route("/welcome", methods=["POST"])
def checkUser():
    form = request.form
    user = form.get("username")
    password = form.get("password")
    if user in db and db[user]["password"] == password:
        session["username"] = user
        return redirect('/welcome')
    else:
        return redirect("/denied")


@app.route('/denied')
def access_denied():
    return render_template("denied.html")


@app.route("/createUser", methods=["POST"])
def createUser():
  form = request.form
  user = form.get("username")
  password = form.get("password")
  name = form.get("name")

  if user in db:
    return "Could not create user"

  db[user] = {"password": password, "name": name}

  return f""" Created user: 
  User: {user}
  Password: {db[user]["password"]}
  Name: {db[user]["name"]}
  """

app.run(host='0.0.0.0', port=81)