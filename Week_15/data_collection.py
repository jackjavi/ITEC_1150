"""
Author: Yusuf Hassan
Date: 2025-05-07
Description: This program allows the user to manage contact information
             stored in a CSV file. Users can view, add, and exit
             the contact management system.
"""
import pyinputplus as pyip
import csv
import os

CONTACT_FILE = 'contacts.csv'

def view_contacts():
    """Reads and displays all contacts from the CSV file with headers."""
    if not os.path.exists(CONTACT_FILE):
        print("\nNo contacts stored yet.\n")
        return

    try:
        with open(CONTACT_FILE, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)  # Read the header row if it exists
            if header:
                print(f"\n{'Name':<20}{'Email':<30}{'Phone':<15}")
                for row in reader:
                    if len(row) == 3:
                        name, email, phone = row
                        print(f"{name:<20}{email:<30}{phone:<15}")
                print("\n")
            else:
                print("\nNo contacts stored yet or the file is empty.\n")
    except Exception as e:
        print(f"Error reading contact file: {e}")

def add_contact():
    """Prompts the user for contact information and adds it to the CSV file."""
    name = pyip.inputStr(prompt="Enter contact's name: ")
    email = pyip.inputEmail(prompt="Enter contact's email: ")
    phone = pyip.inputStr(prompt="Enter contact's phone number: ")

    try:
        file_exists = os.path.exists(CONTACT_FILE)
        with open(CONTACT_FILE, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['Name', 'Email', 'Phone'])  # Write header if file is new
            writer.writerow([name, email, phone])
        print(f"\nContact '{name}' added successfully.\n")
    except Exception as e:
        print(f"Error writing to contact file: {e}")

def main():
    """Main function to run the contact management program."""
    while True:
        print("\nPlease select an option:")
        choices = ['View', 'Add', 'Exit']
        choice = pyip.inputMenu(choices, numbered=True)

        if choice == 'View':
            view_contacts()
        elif choice == 'Add':
            add_contact()
        elif choice == 'Exit':
            print("Thanks for using the contact manager.")
            break

if __name__ == "__main__":
    main()