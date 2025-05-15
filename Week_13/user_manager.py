"""
Author: Yusuf Hassan
Date: 2025-04-22
Description: This program allows the user to manage a list of users
             stored in a text file. Users can view, add, and exit
             the user management system.
"""
import pyinputplus as pyip
import os

USER_FILE = 'users.txt'

def initialize_user_file():
    """Initializes the user file with a default user if it doesn't exist."""
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            f.write('Yusuf Yusuf@gmail.com\n')

def view_users():
    """Reads and displays all users from the user file."""
    try:
        with open(USER_FILE, 'r') as f:
            for line in f:
                username, email = line.strip().split()
                print(f"Username: {username:<10} Email: {email}")
    except FileNotFoundError:
        print(f"Error: The file '{USER_FILE}' was not found.")

def add_users():
    """Prompts the user to enter new users and adds them to the file."""
    users_input = pyip.inputStr(prompt="Enter user(s) in the format 'username email'. Separate multiple users with commas: ")
    new_users = users_input.split(',')
    with open(USER_FILE, 'a') as f:
        for user_entry in new_users:
            user_entry = user_entry.strip()
            if user_entry:  # Avoid writing empty lines
                try:
                    username, email = user_entry.split()
                    if ' ' in username:
                        print(f"Warning: Username '{username}' contains spaces and will not be added.")
                        continue
                    f.write(f"{username} {email}\n")
                    print(f"User '{username}' added successfully.")
                except ValueError:
                    print(f"Warning: Invalid format '{user_entry}'. Please use 'username email'.")

def main():
    """Main function to run the user manager program."""
    initialize_user_file()

    while True:
        print("\nPlease select an option:")
        choices = ['view', 'add', 'exit']
        choice = pyip.inputMenu(choices, numbered=True)

        if choice == 'view':
            view_users()
        elif choice == 'add':
            add_users()
        elif choice == 'exit':
            print("Thanks for using the user manager.")
            break

if __name__ == "__main__":
    main()