"""
Author: Yusuf Hassan
Date: 2025-04-15
Description: This program summarizes a book list, including titles and prices,
             using PyInputPlus for input validation.
"""
import pyinputplus as pyip

def main():  # call functions and save results under key variable names.
    print('Welcome to the book list program.')  # print intro
    try:
        num_books = get_num_books()
        title_price_list = get_book_info(num_books)
        total, average = processing([price for title, price in title_price_list])
        outputs(title_price_list, total, average)
        restart = pyip.inputYesNo(prompt='Do you want to enter more books? (yes/no): ')
        if restart == 'yes':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)

def get_num_books():
    """
    Gets the number of books needed from the user using pyip.inputInt.
    Ensures the input is a positive integer.
    """
    num = pyip.inputNum(prompt='Enter the number of books needed: ',
                        min=1,  # Minimum value is 1
                        limit=3,  # Limit the number of retries
                        timeout=100, # Set a timeout for input
                        default=1  # Default to 1 if no input is given
                        )
    return num

def get_book_info(num_books):
    """
    Collects the title and price for each book from the user using PyInputPlus.
    Validates the price to be a float between $1.00 and $100.00.
    """
    title_price_list = []
    for i in range(num_books):
        title = pyip.inputStr(prompt=f'Enter the title of book #{i + 1}: ',
                              blank=False,
                              strip=True)
        price = pyip.inputFloat(prompt=f'Enter the price of "{title}": $',
                                min=1.00,
                                max=100.00,
                                limit=3,
                                timeout=100,
                                default=1.00)
        title_price_list.append((title.title(), price))  # Store title in Title Case
    return title_price_list

def processing(price_list):
    """
    Calculates the total and average price of the books.
    """
    total = sum(price_list)
    average = total / len(price_list) if price_list else 0
    return total, average

def outputs(title_price_list, total, average):
    """
    Displays the information about each book and the summary (total and average).
    """
    print(f'\nInfo on {len(title_price_list)} Books:')
    print(f'{"Title":<20}{"Price":>10}')
    print('-' * 30)
    for title, price in title_price_list:
        print(f'{title:<20}${price:>8.2f}')
    print('-' * 30)
    print(f'{"Total":<20}${total:>8.2f}')
    print(f'{"Average":<20}${average:>8.2f}')

if __name__ == "__main__":
    main()