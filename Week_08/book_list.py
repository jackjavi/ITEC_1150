"""
Author: Yusuf Hassan
Date: 2025-03-18
Description: This program summarizes a book list, including titles and prices.
"""
print('This program summarizes a book list.')  # print intro

def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        num_books, title_list, price_list = inputs() # Add title list to return values
        total, average = processing(price_list)
        outputs(num_books, title_list, price_list, total, average) # Add title list to parameters
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
    price_list = []  # create list to save prices
    title_list = [] # Create list for titles
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        title = input(f'Enter the book title: ') # Get title
        print(f'Enter the cost of book #{index +1}, to the nearest dollar: ')
        book_cost = get_pos_int()  # call validation function to collect int > 0
        price_list.append(book_cost)  # build price list
        title_list.append(title) # Add title to title list
    return num_books, title_list, price_list # Return titles

def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int

def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list) # add up all of the prices
    price_list_len = len(price_list) # this is how many prices we have
    average = total / price_list_len # calculate the total
    average_rounded = round(average, 2) # round the total

    alt_average = round(total / len(price_list), 2)
    return total, average_rounded

def outputs(num_books, title_list, price_list, total, average):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book #":<20}{"Price":>10}') # Changed header
    for index in range(len(price_list)):
        print(f'{title_list[index]:<20}${price_list[index]:>8.2f}') # Print titles and prices
    print(f'{"Total":<20}${total:>8.2f}') # Adjusted formatting
    print(f'{"Average":<20}${average:>8.2f}') # Adjusted formatting

main()  # call main to start or restart program.