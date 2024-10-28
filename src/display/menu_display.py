from vote_manager import display_live_stats, save_vote
from leaderboard_manager import display_leaderboard

def show_main_menu(matches, username):
    while True:
        print(f"\nWelcome, {username}!")
        print("\n" + "=" * 30)
        print("           WWE Voting Menu")
        print("=" * 30)
        display_live_stats()
        display_leaderboard()
        print("\n1. Vote on a match")
        print("2. View Leaderboard")
        print("3. Logout")
        print("=" * 30)

        choice = input("Choose an option: ")

        if choice == "1":
            vote_on_match(matches, username)
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def vote_on_match(matches, username):
    print("Choose a match to vote on:")
    display_live_stats()  # Display current matches and votes

    match_id = int(input("Enter the match ID you want to vote on: "))
    predicted_winner = input("Enter your predicted winner: ")

    save_vote(match_id, username, predicted_winner)
    print("Vote registered successfully!")
    display_live_stats()  # Display updated stats after voting
