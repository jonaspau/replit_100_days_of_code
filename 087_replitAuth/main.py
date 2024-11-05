from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  username = request.headers["X-Replit-User-Name"]
  return f"Hello {username}"

app.run(host='0.0.0.0', port=81)