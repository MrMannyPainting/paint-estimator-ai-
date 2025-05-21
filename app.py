from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Mr. Manny Paint Estimator is running!"

if __name__ == "__main__":
    app.run()
