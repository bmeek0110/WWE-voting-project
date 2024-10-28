import json
import hashlib

def hash_password(password):
    """Hash the password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user with a hashed password."""
    users = load_users()
    
    # Check if the username already exists
    if any(user['username'] == username for user in users):
        print("Username already exists. Please choose a different one.")
        return False

    # Add new user
    users.append({
        'username': username,
        'password': hash_password(password)
    })

    save_users(users)
    print("User registered successfully.")
    return True

def load_users():
    """Load users from the JSON file."""
    try:
        with open('data/users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_users(users):
    """Save users to the JSON file."""
    with open('data/users.json', 'w') as f:
        json.dump(users, f, indent=4)

def authenticate_user(username, password):
    """Authenticate a user by checking username and hashed password."""
    users = load_users()
    
    for user in users:
        if user['username'] == username and user['password'] == hash_password(password):
            return True
    return False
