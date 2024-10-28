def display_matches(matches):
    print("Current Matches:")
    for match in matches:
        print(f"{match['id']}: {match['title']} - Votes: {match['votes']}")
