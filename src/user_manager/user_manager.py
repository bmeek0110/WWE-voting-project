import json

def load_users():
    try:
        with open('data/users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def authenticate_user(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False
