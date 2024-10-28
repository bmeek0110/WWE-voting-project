from user_manager.user_manager import user_login, user_registration
from display.menu_display import show_main_menu
import json

def main():
    while True:
        print("Welcome to the WWE Voting Application!")
        choice = input("1. Login\n2. Register\n3. Exit\nChoose an option: ")

        if choice == "1":
            username = user_login()
            if username:
                break
        elif choice == "2":
            user_registration()
        elif choice == "3":
            return
        else:
            print("Invalid option. Please try again.")

    try:
        with open('data/matches.json', 'r') as f:
            matches = json.load(f)
    except FileNotFoundError:
        print("No matches found. Please create matches first.")
        return

    show_main_menu(matches, username)

if __name__ == "__main__":
    main()
