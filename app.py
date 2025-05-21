from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Paint Estimator AI is running!"