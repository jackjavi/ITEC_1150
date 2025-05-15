"""
Author: Yusuf Hassan
Date: 2025-03-25
Description: This program manages usernames and full names using a dictionary.
It allows users to view, add, edit, and delete entries.
"""

def main():
    try:
        users = {'hhassan': 'hassan hassan', 'jsmith': 'jake smith', 'acooper': 'ann cooper'}
        display_menu()
        while True:
            command = input('Command: ').lower()
            if command == 'view':
                view(users)
            elif command == 'add':
                add(users)
            elif command == 'del':
                delete(users)
            elif command == 'edit':
                edit(users)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')

def display_menu():
    print('COMMAND MENU')
    print('view - View user name')
    print('add - Add a user')
    print('edit - Edit a user')
    print('del - Delete a user')
    print('exit - Exit program')
    print()

def view(users):
    display_usernames(users)
    username = input('Enter username to view: ').lower()
    if username in users:
        name = users[username]
        print('Full name: ' + name.title() + '.\n')
    else:
        print('There is no user with that username. \n')

def add(users):
    display_usernames(users)
    username = input('Enter new username to add: ').lower()
    if username in users:
        print('Error: Username already exists. \n')
        return
    fullname = input('Enter full name: ')
    users[username] = fullname
    print(fullname.title(), 'was added. \n')

def delete(users):
    display_usernames(users)
    username = input('Enter username to delete: ').lower()
    if username not in users:
        print('Error: Username does not exist. \n')
        return
    fullname = users.pop(username)
    print(fullname.title(), 'was deleted. \n')

def edit(users):
    display_usernames(users)
    username = input('Enter username to edit: ').lower()
    if username not in users:
        print('Error: Username does not exist. \n')
        return
    fullname = input('Enter the new full name of the user: ')
    users[username] = fullname
    print(f'{username} has been updated to the full name {fullname.title()}. \n')

def display_usernames(users):
    """Displays the keys from the passed-in dictionary"""
    usernames = list(users.keys())
    usernames.sort()
    line = 'Usernames: '
    for username in usernames:
        line += username + ' '
    print(line)

if __name__ == '__main__':
    main()