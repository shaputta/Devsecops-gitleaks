
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/apikey')
def get_key():
    api_key = os.getenv("API_KEY", "No API key found")
    return jsonify({"api_key": api_key})

@app.route('/')
def home():
    return jsonify({"message": "Flask app running. Use /apikey to get the API key."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)