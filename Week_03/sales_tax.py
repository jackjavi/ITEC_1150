"""
Author: Yusuf Hassan
Date: 2025-02-04
Description: This program asks the user to enter the price of a purchase order
    - Calculates state sales tax at 5%.
    - Calculates county sales tax at 2.5%.
And outputs a sales report showing Purchase Order Price,
State Tax, County Tax, and Grand Total.
"""

# Constants for tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get purchase order amount from user
purchase_amount = float(input("What is the total price of your purchase order? "))

# Calculate taxes
state_tax = round(purchase_amount * STATE_TAX_RATE, 2)
county_tax = round(purchase_amount * COUNTY_TAX_RATE, 2)

# Calculate grand total
grand_total = round(purchase_amount + state_tax + county_tax, 2)

# Display sales report
print("\nCustom Delivery Sales Receipt")
print('{:<10}{:>8}{:>15.2f}'.format('PO Amount', '$', purchase_amount))
print('{:<10}{:>8}{:>15.2f}'.format('State Tax', '$', state_tax))
print('{:<10}{:>8}{:>15.2f}'.format('County Tax', '$', county_tax))
print('{:<10}{:>8}{:>15.2f}'.format('Total', '$', grand_total))