# app.py
import os

def connect_to_service():
    # ❌ Hardcoded API key — will be caught by GitLeaks (generic-api-key / AWS / Token patterns)
    API_KEY = "ghp_AbC12345FakeGitHubToken9876543210"
    
    print("Connecting to external service with provided API key...")
    print(f"Using API_KEY: {API_KEY[:6]}********")

    return True

if __name__ == "__main__":
    connect_to_service()