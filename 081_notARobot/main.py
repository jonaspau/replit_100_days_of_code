from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  page = ""
  f = open("templates/form.html", "r")
  page = f.read()
  f.close()
  return page


@app.route('/processForm', methods=(['POST']))
def process_form():
  form_data = request.form.to_dict()
  # Display the JSON directly:
  # return jsonify(form_data)

  
  page = ""
  made_of_metal = request.form.get("made_of_metal")
  infinityPlus1 = request.form.get("infinity_plus_1", "").lower()
  teamUp = request.form.get("team_up")
  

  if made_of_metal == "no" and infinityPlus1 != "error" and teamUp == "humans":
    f = open("templates/human.html", "r")
  else:
    f = open("templates/robot.html", "r")

  page = f.read()
  f.close()
  return page
    
app.run(host='0.0.0.0', port=81)