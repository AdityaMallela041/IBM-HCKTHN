from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

WATSON_API_KEY = os.getenv("WATSON_API_KEY")
WATSON_URL = os.getenv("WATSON_URL")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

@app.route('/')
def home():
    return "✅ Upgraded Smart City Assistant backend is running!"

@app.route('/api/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get("question", "")

    # Simulate Granite LLM response
    simulated_answer = f"🌿 Simulated Granite LLM response for: '{question}' — Aim to reduce water and energy usage by 15% this month."

    return jsonify({
        "response": simulated_answer
    })

@app.route('/api/sustainability-tips', methods=['GET'])
def tips():
    return jsonify({
        "tips": [
            "Use public transport to reduce carbon footprint.",
            "Install low-flow showerheads to save water.",
            "Segregate waste to improve recycling rates."
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
