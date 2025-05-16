"""
Author: Yusuf Hassan
Date: 2025-05-15
Description: This program allows the user to build one or more virtual pizzas by selecting from
             dynamically loaded ingredients and prices from a web-hosted JSON file.
             It calculates and displays the cost of each pizza and the total cost of the order,
             formatting the output to align prices.
"""
import pyinputplus as pyip
import requests
import json

# URL for the ingredients JSON file
INGREDIENTS_URL = "https://itec-minneapolis.s3.us-west-2.amazonaws.com/ingredients.json"

def fetch_ingredients_data(url):
    """
    Fetches ingredient data from a given URL and parses it as JSON.
    Handles network and JSON decoding errors.
    """
    try:
        print(f"Downloading ingredients from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        ingredients_data = json.loads(response.text)
        print("Ingredients downloaded successfully.")
        return ingredients_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} (Status Code: {response.status_code}). "
              "Could not fetch ingredients. Please check the URL or your network.")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}. "
              "Could not connect to the internet. Please check your network connection.")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}. "
              "The request took too long. Please try again.")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected request error occurred: {req_err}.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {url}. The content might not be valid JSON.")
    return None

def get_pizza_ingredients(base_options_data, toppings_data):
    """
    Asks the user for their pizza preferences based on the fetched ingredient data.
    Returns a list of selected ingredient names.
    """
    selected_ingredients = []

    # Get base options (crust, sauce, cheese)
    for category_data in base_options_data:
        category_name = category_data['category'].capitalize()
        options = category_data['options']
        
        if not options:
            print(f"No options available for {category_name}.")
            continue

        # Prepare choices for PyInputPlus menu
        choices = list(options.keys())
        
        choice = pyip.inputMenu(
            choices,
            prompt=f"What type of {category_name} would you like?\n",
            numbered=True,
        )
        selected_ingredients.append(choice)

    # Get toppings
    if toppings_data:
        want_toppings = pyip.inputYesNo(prompt="Do you want any toppings? (yes/no):\n")
        if want_toppings == "yes":
            # Allow multiple toppings
            while True:
                topping_choices = list(toppings_data.keys())
                if not topping_choices:
                    print("No toppings available.")
                    break
                
                # Add 'done' option to exit topping selection, matching the instruction image
                topping_choices_display = topping_choices + ["done"]
                
                chosen_topping = pyip.inputMenu(
                    topping_choices_display,
                    prompt="What toppings would you like? (Enter 'done' when finished):\n",
                    numbered=True,
                )
                
                if chosen_topping.lower() == "done": # Check for lowercase 'done'
                    break
                else:
                    selected_ingredients.append(chosen_topping)
                    print(f"'{chosen_topping}' added.")
    else:
        print("No topping options available.")

    return selected_ingredients

def calculate_pizza_cost(ingredients, all_ingredients_data):
    """
    Calculates the cost of a single pizza based on selected ingredients
    and the full ingredients data (which contains prices).
    """
    cost = 0
    
    # Create a unified price dictionary for easy lookup
    unified_prices = {}
    for category_data in all_ingredients_data.get('base_options', []):
        unified_prices.update(category_data['options'])
    unified_prices.update(all_ingredients_data.get('toppings', {}))

    for ingredient_name in ingredients:
        price = unified_prices.get(ingredient_name)
        if price is not None:
            cost += price
        else:
            print(f"Warning: Price not found for ingredient '{ingredient_name}'. Skipping.")
    return cost

def main():
    """Main function to run the Pizza Ordering program."""
    print("Welcome to the Dynamic Pizza Order System!")

    # Fetch all ingredients data from the web
    all_ingredients_data = fetch_ingredients_data(INGREDIENTS_URL)
    if not all_ingredients_data:
        print("Failed to load ingredients. Exiting program.")
        return

    base_options_data = all_ingredients_data.get('base_options', [])
    toppings_data = all_ingredients_data.get('toppings', {})

    if not base_options_data and not toppings_data:
        print("No base options or toppings found in the ingredients data. Exiting program.")
        return

    num_pizzas = pyip.inputInt(
        prompt="How many pizzas would you like to order? ",
        min=1,
    )

    all_pizzas_ingredients = []
    for i in range(num_pizzas):
        print(f"\n--- Building Pizza #{i+1} ---")
        ingredients = get_pizza_ingredients(base_options_data, toppings_data)
        if ingredients: # Only add if some ingredients were selected
            all_pizzas_ingredients.append(ingredients)
        else:
            print("No ingredients selected for this pizza. Skipping.")

    if not all_pizzas_ingredients:
        print("\nNo pizzas were ordered. Goodbye!")
        return

    total_order_cost = 0
    print("\nYour Full Order Summary")
    
    # 1. Calculate the maximum length needed for the label column
    max_label_width = max(len("Grand Total:"), len("Total for Pizza #99:")) 
    
    #    Iterate through all chosen ingredients to find the longest capitalized name
    for pizza_ingredients in all_pizzas_ingredients:
        for ingredient in pizza_ingredients:
            if len(ingredient.capitalize()) > max_label_width:
                max_label_width = len(ingredient.capitalize())
    
    #    Add a small buffer for aesthetic spacing
    max_label_width += 3 

    # Calculate the length of the separator line
    # It's the length of the leading spaces (2) + label_width + $ (2) + price (8)
    separator_length = 2 + max_label_width + 2 + 8 
    
    print("-" * separator_length) # Separator

    for i, ingredients_list in enumerate(all_pizzas_ingredients):
        print(f"\nPizza #{i+1}:")
        pizza_subtotal = 0
        
        # Create a unified price dictionary for current pizza display
        unified_prices = {}
        for category_data in all_ingredients_data.get('base_options', []):
            unified_prices.update(category_data['options'])
        unified_prices.update(all_ingredients_data.get('toppings', {}))

        for ingredient in ingredients_list:
            price = unified_prices.get(ingredient)
            if price is not None:
                print(f"  {ingredient.capitalize():<{max_label_width}} {'$':>2} {price:>6.2f}")
                pizza_subtotal += price
            else:
                print(f"  {ingredient.capitalize():<{max_label_width}} {'$':>2} {'N/A':>6}") 
        
        total_order_cost += pizza_subtotal
        
        pizza_total_label = f"Total for Pizza #{i+1}:"
        print(f"  {pizza_total_label:<{max_label_width}} {'$':>2} {pizza_subtotal:>6.2f}")
        print("-" * separator_length)

    print(f"\n{'Grand Total:':<{max_label_width + 2}} {'$':>2} {total_order_cost:>6.2f}")
    print("-" * separator_length)
    print("-" * separator_length)
    print("\nYour order has been placed! Thank you for oordering with us.\n")

if __name__ == "__main__":
    main()
