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
    
    keywords = {
        "water": "💧 Conserve water by fixing leaks and using low-flow fixtures.",
        "energy": "⚡ Save energy by switching to LED bulbs and unplugging devices.",
        "transport": "🚌 Use eco-friendly transport options like cycling or public transit.",
        "recycle": "♻️ Separate recyclables and compost organic waste.",
        "default": "🌿 Think sustainably! Try reducing single-use plastics and being mindful of your footprint."
    }

    keyword_matched = next((tip for key, tip in keywords.items() if key in question.lower()), keywords["default"])
    simulated_answer = f"Granite LLM Suggestion: {keyword_matched}"
    

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
