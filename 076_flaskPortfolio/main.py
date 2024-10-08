from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path="/static") # No path to the static folder to get images etc


@app.route('/')
def index(): 
  page = f"""<html><body>
  <p><a href = "/portfolio">Portfolio</a></p>
  <p><a href = "/linktree">Linktree</a></p>
  </body>
  </html>"""
  return page

@app.route('/portfolio') 
def portfolio(): #Two subroutines with the same name. 
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="static/styles/portfolio.css" rel="stylesheet" type="text/css" />
  <link href='https://fonts.googleapis.com/css?family=Josefin+Sans:700' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
</head>

<body>
  <div class="content">
    <h1>Jonas' Portfolio</h1>
    <p class="intro">As a side project I've been doing Replit's 100 days of code challenge. Here are some of the projects I've made.</p>
    <div class="cards">
      <div class="card">
        <div class="container">
          <a href="https://github.com/jonaspau/replit_100_days_of_code/blob/main/071_login.py"><img src="/static/images/login.png"></a>
          <h2 class=>Login system</h2>
          <div class="hline"></div>
          <p>A login system that makes it possible to either create a user or log in. The user is stored in the replit-db and the password is salted and hashed.</p>
        </div>  
      </div>
      <div class="card">
        <div class="container">
          <a href="https://github.com/jonaspau/replit_100_days_of_code/blob/main/072_secretKeeper2.py"><img src="/static/images/secretkeeper.png"></a>
          <h2>Secret keeper</h2>
          <div class="hline"></div>
          <p>The secret keeper use replit db to handle login and storing of secrets. </p>
          <p>At first run you'll have to set a password and on any subsequent logins the password has to be validated before seeing the secrets.</p>
        </div>
      </div>
      <div class="card">
        <div class="container">
          <img src="/static/images/calculator.png">
          <h2>Calculator</h2>
          <div class="hline"></div>
          <p>As a project to create a simple graphical interface with tkinter I made this calculator.</p>
        </div>
      </div>
      <div class="card">
        <div class="container">
          <h2>Todo-list</h2>
          <div class="hline"></div>
          <p>A simple todo-list wich stores to a file and backs up said file in case of errors.</p>
          <a href=https://github.com/jonaspau/replit_100_days_of_code/blob/main/055_todoBackup.py>See the to-do-list on
            Github</a>
        </div>
      </div>
      <div class="card">
        <div class="container">
          <h2>The Bird-app</h2>
          <div class="hline"></div>
          <p>The birdapp is a simple text-interface version of the blue bird-app that has been renamed</p>
          <a href="https://github.com/jonaspau/replit_100_days_of_code/blob/main/061_birdApp.py">See the Bird-app on Github</a>
        </div>
      </div>
    </div>
  </div>
</body>

</html>"""

  return page

@app.route('/linktree') 
def linktree(): #Two subroutines with the same name. 
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="/static/styles/style.css" rel="stylesheet" type="text/css" />
  <link href='https://fonts.googleapis.com/css?family=Josefin+Sans:700' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
</head>

<body>
  <div class="content">
    <h1>Jonas Paulsen</h1>
    <img src="/static/images/jonasPaulsen.jpg" class="profilepic">
    <p class="topic">Location:</p>
    <ul>
      <li>City: Ski</li>
      <li>Country: Norway</li>
    </ul>
    <p class="topic">Social media:</p>
    <ul>
      <li><a href="https://www.linkedin.com/in/jonaspaulsen/">Linkedin</a></li>
      <li><a href="https://github.com/jonaspau">Github</a></li>
      <li><a href="https://jpaulsen.net/">Webpage</a></li>
    </ul>
  </div>
  <script src="script.js"></script>

</body>

</html>"""

  return page

app.run(host='0.0.0.0', port=81) # Missed the run command