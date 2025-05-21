
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Paint Estimator AI is running!"

@app.route("/estimate", methods=["POST"])
def estimate():
    data = request.json
    # Aquí iría la lógica real del estimado de pintura
    response = {
        "address": data.get("address"),
        "estimate": "Pending - logic not implemented"
    }
    return jsonify(response)
