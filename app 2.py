
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Paint Estimator AI is running!"
