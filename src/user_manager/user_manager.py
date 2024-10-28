from auth_manager import register_user, authenticate_user

def user_login():
    """Handle user login."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if authenticate_user(username, password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def user_registration():
    """Handle user registration."""
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    
    if register_user(username, password):
        print("Registration successful!")
        return username
    else:
        print("Registration failed. Please try again.")
        return None
