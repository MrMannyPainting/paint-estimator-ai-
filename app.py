from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Paint Estimator AI is running!"

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.json
    square_feet = data.get('square_feet', 0)
    rate = data.get('rate', 1.75)
    total = square_feet * rate
    return jsonify({'estimate': total})