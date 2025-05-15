"""
Author: Yusuf Hassan
Date: 2025-02-04
Description: This program asks the user for:
    - the number of cups sold for each drink type (coffee, tea, cappuccino)
    - the price per cup for each drink
Calculates and displays total sales for each drink
& the total sales overall in a table format.
"""

# Get user input
coffee_cups = int(input("Enter the number of cups of coffee sold: "))
tea_cups = int(input("Enter the number of cups of tea sold: "))
cappuccino_cups = int(input("Enter the number of cups of cappuccino sold: "))

coffee_price = float(input("Enter the price per cup of coffee: "))
tea_price = float(input("Enter the price per cup of tea: "))
cappuccino_price = float(input("Enter the price per cup of cappuccino: "))

# Calculate total sales
coffee_total = coffee_cups * coffee_price
tea_total = tea_cups * tea_price
cappuccino_total = cappuccino_cups * cappuccino_price
sum_of_items = coffee_cups + tea_cups + cappuccino_cups
total_sales = coffee_total + tea_total + cappuccino_total

# Display results in table format
print('{:<15}{:>10}{:>6}{:>8}{:>6}{:>12}'.format('Drink Type', 'Cups Sold', '', 'Price', '', 'Total'))
print('{:<15}{:>10}{:>6}{:>8.2f}{:>6}{:>12.2f}'.format('Coffee', coffee_cups, '$', coffee_price, '$', coffee_total))
print('{:<15}{:>10}{:>6}{:>8.2f}{:>6}{:>12.2f}'.format('Tea', tea_cups, '$', tea_price, '$', tea_total))
print('{:<15}{:>10}{:>6}{:>8.2f}{:>6}{:>12.2f}'.format('Cappuccino', cappuccino_cups, '$', cappuccino_price, '$', cappuccino_total))
print('{:<15}{:>10}{:>6}{:>8}{:>6}{:>12.2f}'.format('Total', sum_of_items, '', '', '$', total_sales))