from vote_manager import display_live_stats, save_vote
from leaderboard_manager import display_leaderboard

def clear_screen():
    """Clear the console screen (works on most systems)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print the header with a title."""
    print("\033[1;34m" + "=" * 50 + "\033[0m")
    print(f"\033[1;36m{title:^50}\033[0m")
    print("\033[1;34m" + "=" * 50 + "\033[0m")

def show_main_menu(matches, username):
    while True:
        clear_screen()
        print_header("WWE Voting Menu")
        print(f"\n\033[1;32mWelcome, {username}!\033[0m")
        print("\n" + "=" * 30)
        print("           WWE Voting Menu")
        print("=" * 30)
        display_live_stats()
        display_leaderboard()
        print("\n\033[1;33m1. Vote on a match\033[0m")
        print("\033[1;33m2. View Leaderboard\033[0m")
        print("\033[1;31m3. Logout\033[0m")
        print("=" * 30)

        choice = input("\033[1;37mChoose an option: \033[0m")

        if choice == "1":
            vote_on_match(matches, username)
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            print("\033[1;36mLogging out...\033[0m")
            break
        else:
            print("\033[1;31mInvalid option. Please try again.\033[0m")

def vote_on_match(matches, username):
    clear_screen()
    print_header("Vote On Matches")
    print("\033[1;32mChoose a match to vote on:\033[0m")
    display_live_stats()  # Display current matches and votes

    match_id = int(input("Enter the match ID you want to vote on: "))
    predicted_winner = input("\033[1;37mEnter your predicted winner: \033[0m")

    save_vote(match_id, username, predicted_winner)
    print("\033[1;36mVote registered successfully!\033[0m")
    display_live_stats()  # Display updated stats after voting
