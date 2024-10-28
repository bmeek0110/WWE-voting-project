import json
from datetime import datetime
from leaderboard_manager import update_leaderboard

def save_vote(match_id, username, predicted_winner):
    vote_data = {
        "match_id": match_id,
        "username": username,
        "predicted_winner": predicted_winner,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Load existing votes
    try:
        with open('data/events.json', 'r') as f:
            votes = json.load(f)
    except FileNotFoundError:
        votes = []

    # Append the new vote
    votes.append(vote_data)

    # Save the updated votes back to the file
    with open('data/events.json', 'w') as f:
        json.dump(votes, f, indent=4)

    # Update the match vote count
    update_vote_count(match_id)

    # Update the leaderboard with the new vote
    update_leaderboard(username)

def update_vote_count(match_id):
    # Load existing matches
    try:
        with open('data/matches.json', 'r') as f:
            matches = json.load(f)
    except FileNotFoundError:
        print("No matches found to update vote count.")
        return

    for match in matches:
        if match['id'] == match_id:
            match['votes'] += 1  # Increment the vote count
            break

    # Save the updated matches back to the file
    with open('data/matches.json', 'w') as f:
        json.dump(matches, f, indent=4)

def display_live_stats():
    # Load existing matches
    try:
        with open('data/matches.json', 'r') as f:
            matches = json.load(f)
    except FileNotFoundError:
        print("No matches found.")
        return

    print("\n--- Live Voting Stats ---")
    for match in matches:
        print(f"{match['title']} - Votes: {match['votes']}")
