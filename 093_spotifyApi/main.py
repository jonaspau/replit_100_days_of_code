from flask import Flask, render_template, request
import spotify
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    year = request.form['year']  # Correctly access the form data
    token = spotify.authenticate()

    results = spotify.search(token, year)
    return render_template("index.html", tracks=results, year=year)
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
