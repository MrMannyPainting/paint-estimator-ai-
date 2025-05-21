
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Paint Estimator AI is running!"

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.get_json()

    # Simulación de lógica para estimación de pintura
    square_feet = data.get('square_feet', 0)
    coats = data.get('coats', 2)
    coverage_per_gallon = 350  # pies cuadrados por galón

    gallons_needed = (square_feet * coats) / coverage_per_gallon

    return jsonify({
        "square_feet": square_feet,
        "coats": coats,
        "estimated_gallons": round(gallons_needed, 2)
    })

if __name__ == '__main__':
    app.run()
