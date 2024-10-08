from flask import Flask

app = Flask(__name__)

reflections = {}

reflections["78"] = {"link": "", "reflection": "Today's task! Feels kind of iffy as I'll have to manually update a dictionary to create new html pages."}
reflections["77"] = {"link": "", "reflection": "Finally, done with the boring html and css-stuff"}
reflections["76"] = {"link": "", "reflection": "Was hoping to actually create dynamic content, but was stuck with pure html and css in flask."}

@app.route('/')

def index():
  return "Enter a lesson number in the url"

@app.route('/<pageNumber>')

def lesson(pageNumber):
  page = ""
  f = open("templates/reflection.html", "r")
  page = f.read()
  f.close()

  # Rewrite the page template with values from the dictionary
  page = page.replace("{lesson}", pageNumber)
  page = page.replace("{link}", reflections[pageNumber]["link"])
  page = page.replace("{reflection}", reflections[pageNumber]["reflection"])
  
  return page

app.run(host='0.0.0.0', port=81)