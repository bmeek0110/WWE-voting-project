import json

def update_leaderboard(username):
    try:
        with open('data/leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = []

    # Check if user is already on the leaderboard
    for entry in leaderboard:
        if entry['username'] == username:
            entry['votes'] += 1
            break
    else:
        # Add new user if not found
        leaderboard.append({'username': username, 'votes': 1})

    with open('data/leaderboard.json', 'w') as f:
        json.dump(leaderboard, f, indent=4)

def display_leaderboard():
    try:
        with open('data/leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        print("No leaderboard data found.")
        return

    # Sort the leaderboard by votes
    leaderboard.sort(key=lambda x: x['votes'], reverse=True)

    print("\n--- Leaderboard ---")
    for entry in leaderboard:
        print(f"{entry['username']}: {entry['votes']} votes")
