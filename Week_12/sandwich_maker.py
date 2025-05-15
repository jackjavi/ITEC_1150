"""
Author: Yusuf Hassan
Date: 2025-04-15
Description: This program allows the user to build one or more virtual sandwiches by selecting from a menu of bread, protein, cheese, and extra ingredients.
             It calculates and displays the cost of each sandwich and the total cost of the order, formatting the output to align prices.
"""
import pyinputplus as pyip

# Prices for ingredients
prices = {
    "white": 1.95,
    "wheat": 2.25,
    "sourdough": 2.50,
    "chicken": 2.75,
    "turkey": 2.50,
    "ham": 2.25,
    "tofu": 1.99,
    "cheddar": 0.50,
    "swiss": 0.60,
    "mozzarella": 0.75,
    "mayo": 0.10,
    "mustard": 0.15,
    "lettuce": 0.20,
    "tomato": 0.25,
}

def get_sandwich_ingredients():
    """Asks the user for their sandwich preferences."""
    ingredients = []

    # Get bread choice
    bread_choice = pyip.inputMenu(
        ["White", "Wheat", "Sourdough"],
        prompt="What type of bread would you like?\n",
        numbered=True,
    ).lower()  # Convert to lowercase
    ingredients.append(bread_choice)

    # Get protein choice
    protein_choice = pyip.inputMenu(
        ["Chicken", "Turkey", "Ham", "Tofu"],
        prompt="What protein would you like?\n",
        numbered=True,
    ).lower()  # Convert to lowercase
    ingredients.append(protein_choice)

    # Ask for cheese
    want_cheese = pyip.inputYesNo(prompt="Do you want cheese? (yes/no):\n")
    if want_cheese == "yes":
        cheese_choice = pyip.inputMenu(
            ["Cheddar", "Swiss", "Mozzarella"],
            prompt="What type of cheese would you like?\n",
            numbered=True,
        ).lower()  # Convert to lowercase
        ingredients.append(cheese_choice)

    # Ask for extras
    if pyip.inputYesNo(prompt="Do you want mayo? (yes/no):\n") == "yes":
        ingredients.append("mayo")
    if pyip.inputYesNo(prompt="Do you want mustard? (yes/no):\n") == "yes":
        ingredients.append("mustard")
    if pyip.inputYesNo(prompt="Do you want lettuce? (yes/no):\n") == "yes":
        ingredients.append("lettuce")
    if pyip.inputYesNo(prompt="Do you want tomato? (yes/no):\n") == "yes":
        ingredients.append("tomato")

    return ingredients

def calculate_sandwich_cost(ingredients):
    """Calculates the cost of a single sandwich."""
    cost = 0
    for ingredient in ingredients:
        cost += prices.get(ingredient, 0)
    return cost

def main():
    """Main function to run the sandwich maker program."""
    num_sandwiches = pyip.inputInt(
        prompt="How many sandwiches would you like to order? ",
        min=1,
    )

    all_sandwiches_ingredients = []
    for i in range(num_sandwiches):
        print(f"\nBuilding sandwich #{i+1}...")
        ingredients = get_sandwich_ingredients()
        all_sandwiches_ingredients.append(ingredients)

    total_order_cost = 0
    print("\nYour order:")
    for i, ingredients in enumerate(all_sandwiches_ingredients):
        sandwich_cost = calculate_sandwich_cost(ingredients)
        total_order_cost += sandwich_cost
        print(f"Sandwich #{i+1}:")
        sandwich_subtotal = 0
        for ingredient in ingredients:
            price = prices.get(ingredient, 0)
            print(f"  {ingredient.capitalize():<10} {'$':>2} {price:>6.2f}")
            sandwich_subtotal += price
        print("{:<12} {:>2} {:>6.2f}\n".format("Subtotal:", '$', sandwich_subtotal))

    print("{:<12} {:>2} {:>6.2f}".format("Total:", '$', total_order_cost))

if __name__ == "__main__":
    main()