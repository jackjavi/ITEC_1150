"""
Author: Yusuf Hassan
Date: 2025-03-25
Description: This program summarizes a book list, including titles and prices, using a dictionary.
"""
print('This program summarizes a book list.')  # print intro

def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        book_data = inputs()  # Get book data as a dictionary
        total, average = processing(book_data)
        outputs(book_data, total, average)  # Pass book data dictionary
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development

def inputs():  # collect info needed from the user.
    print('Enter the number of books that you need ')  # user sets the list length/ repetitions of the for loop
    num_books = get_pos_int()  # call validation function to collect int > 0
    book_data = {}  # Create dictionary to store book titles and prices
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        title = input(f'Enter the book title: ')  # Get title
        print(f'Enter the cost of book #{index + 1}, to the nearest dollar: ')
        book_cost = get_pos_int()  # call validation function to collect int > 0
        book_data[title] = book_cost  # Add title and price to dictionary
    return book_data  # Return dictionary

def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int

def processing(book_data):  # use the dictionary to calculate summary data
    prices = list(book_data.values())  # Get list of prices from dictionary values
    total = sum(prices)  # add up all of the prices
    price_list_len = len(prices)  # this is how many prices we have
    average = total / price_list_len  # calculate the total
    average_rounded = round(average, 2)  # round the total
    return total, average_rounded

def outputs(book_data, total, average):  # display information about each book, and summary info
    print(f'Info on {len(book_data)} Books Needed')  # Use length of dictionary
    print(f'{"Book":<20}{"Price":>10}')  # Changed header
    for title, price in book_data.items():  # Iterate through dictionary items
        print(f'{title:<20}${price:>8.2f}')  # Print titles and prices from dictionary
    print(f'{"Total":<20}${total:>8.2f}')  # Adjusted formatting
    print(f'{"Average":<20}${average:>8.2f}')  # Adjusted formatting

main()  # call main to start or restart program.