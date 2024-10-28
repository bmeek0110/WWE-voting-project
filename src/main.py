import json
from display.menu_display import show_main_menu

def main():
    # Load matches from matches.json
    try:
        with open('data/matches.json', 'r') as f:
            matches = json.load(f)
    except FileNotFoundError:
        print("No matches found. Please create matches first.")
        return

    username = input("Enter your username: ")

    show_main_menu(matches, username)  # Pass the matches and username to the main menu

if __name__ == "__main__":
    main()
