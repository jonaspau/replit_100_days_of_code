from flask import Flask, request, render_template

app = Flask(__name__)

users = {"jp": {"user": "jp","email": "jp@jp.com", "password": "jp"},
         "a": {"user": "a", "email": "a@a.com", "password": "a"},
         "b": {"user": "b", "email": "b@b.com", "password": "b"},
        }

@app.route("/login", methods=["POST"])

def login():
  form = request.form
  username = form.get("username")
  email = form.get("email")
  password = form.get("password")
  
  if username in users:
    if email == users[username]["email"] and password == users[username]["password"]:
      return "Congratulations"
    else:
      return "Sorry"
  else:
    return "Sorry"

@app.route('/')
def index():
    return render_template("loginForm.html")
  
app.run(host='0.0.0.0', port=81)