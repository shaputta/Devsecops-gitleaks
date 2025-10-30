# # app.py
# import os

# def connect_to_service():
#     # ❌ Hardcoded API key — will be caught by GitLeaks (generic-api-key / AWS / Token patterns)
#     API_KEY = "ghp_abCDeFgHijKLMNOPqrstuVWxyZ012345678"
    
#     print("Connecting to external services with the provided API key...")
#     print(f"Using API_KEY: {API_KEY[:6]}********")

#     return True

# if __name__ == "__main__":
#     connect_to_service()


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