
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Python Flask backend running successfully"
    })

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    # Demo authentication
    if email and password:
        return jsonify({
            "success": True,
            "user": {
                "email": email,
                "role": "candidate"
            }
        })

    return jsonify({
        "success": False,
        "message": "Invalid credentials"
    }), 401

@app.route("/api/analyze", methods=["POST"])
def analyze():
    return jsonify({
        "score": 88,
        "confidence": 9.1,
        "clarity": 8.7,
        "message": "AI analysis completed successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
