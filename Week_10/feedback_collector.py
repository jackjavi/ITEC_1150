"""
Author: Yusuf Hassan
Date: 2025-04-01
Description: Collects feedback phrases from the user, processes them, and displays them.
"""

def main():
    """
    Main function to get input, validate, call processing, and display the result.
    """
    print("Welcome to the feedback generator.")
    while True:
        feedback_input = input("Please enter multiple feedback phrases, each ending in an exclamation point.\n"
                               "Enter as many as you like. You don't have to capitalize: ")
        if feedback_input and "!" in feedback_input:
            break
        else:
            print("Please enter at least one phrase ending with an exclamation point.")

    feedback_list = processing(feedback_input)
    print("Here are your feedback phrases:")
    for i in range(len(feedback_list)):
        print(f"{i + 1}: {feedback_list[i]}!") # access by index

    print("Thanks for helping us build our feedback library.")

def processing(feedback_input):
    """
    Processes the input string and returns a list of capitalized feedback phrases.
    """
    phrases = feedback_input.split("!")
    processed_phrases = []
    for phrase in phrases:
        phrase = phrase.strip()
        if phrase:  # Check if phrase is not empty after stripping
            processed_phrases.append(phrase.capitalize())

    return processed_phrases

if __name__ == "__main__":
    main()