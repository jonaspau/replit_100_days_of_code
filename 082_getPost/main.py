from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  data = request.args
  lang = data.get("lang", "").lower()
  page = ""
  
  if lang == "no":
    f = open("templates/norwegian.html", "r")
  else:
    f = open("templates/english.html", "r")

  page = f.read()
  f.close()
  
  return page

app.run(host='0.0.0.0', port=81)