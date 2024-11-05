from flask import Flask, request, render_template
from replit import db
from werkzeug.utils import redirect


app = Flask(__name__, static_url_path='/static')


def read_template(file_name):
  with open(f"templates/{file_name}", "r") as file:
      return file.read()
    

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/login")
def login():
  return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route("/welcome", methods=["POST"])
def checkUser():
    form = request.form
    user = form.get("username")
    password = form.get("password")
  
    if user in db and db[user]["password"] == password:
        name = db[user]["name"]
        page = read_template("welcome.html").replace("{name}", name)
        return page
    else:
        return redirect("denied.html")


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