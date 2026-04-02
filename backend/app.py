from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import health_chatbot
from severity import check_severity
import json
import os

app = Flask(__name__)
CORS(app)

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    blood_group = data.get('blood_group')
    emergency_contact = data.get('emergency_contact')
    
    if not username or not password:
        return jsonify({"message": "Username and password required", "status": "failed"})
    
    users = load_users()
    
    # Check if username already exists
    for user in users:
        if user['username'] == username:
            return jsonify({"message": "Username already exists", "status": "failed"})
    
    # Add new user
    users.append({
        "username": username,
        "password": password,
        "blood_group": blood_group,
        "emergency_contact": emergency_contact
    })
    
    save_users(users)
    return jsonify({"message": "Registration successful! Please login.", "status": "success"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password required", "status": "failed"})
    
    users = load_users()
    
    # Find user
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                return jsonify({"message": "Login successful!", "status": "success"})
            else:
                return jsonify({"message": "Incorrect password", "status": "failed"})
    
    return jsonify({"message": "User not found", "status": "failed"})

@app.route('/sos', methods=['POST'])
def sos():
    data = request.json
    lat = data['latitude']
    lon = data['longitude']

    print("Emergency Location:", lat, lon)

    return jsonify({"message": "SOS alert sent! Location shared and hospitals suggested."})


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    reply = health_chatbot(user_message)
    severity = check_severity(user_message)

    return jsonify({"reply": reply + " | Severity Level: " + severity})

@app.route('/user/<username>')
def get_user(username):
    users = load_users()
    for user in users:
        if user['username'] == username:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)