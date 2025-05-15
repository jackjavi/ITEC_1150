"""
Author: Yusuf Hassan
Date: 2025-02-18
Description: This program asks the user how many textbooks they need to buy,
    then asks for the price of each book and calculates the subtotal
    and grand total.
"""

while True:
    num_books_str = input("How many textbooks do you have to buy? ")
    if num_books_str.isnumeric():
        num_books = int(num_books_str)
        if num_books > 0:
            break
        else:
            print("Please enter a positive whole number.")
    else:
        print("Please enter a positive whole number.")

grand_total = 0.0

for book_num in range(1, num_books + 1):
    while True:
        price_str = input(f"Enter price for book #{book_num}: ")
        if price_str.isnumeric():
            price = int(price_str) # Convert to integer if it's numeric
            if price >= 0:
                break
            else:
                print("Price cannot be negative. Please enter a valid price.")
        else:
            print("Invalid input. Please enter a whole number for the price.")

    grand_total += price
    print(f"\tSubtotal ${grand_total:.2f}.")

print(f"Grand total = ${grand_total:.2f}.")