"""
Author: Yusuf Hassan
Date: 2025-04-29
Description: This program downloads a text file from a specified URL
             and displays its contents to the console.
"""
import requests

def main():
    url = "https://www.unicode.org/Public/MAPPINGS/ISO8859/8859-1.TXT"

    try:
        print(f"Downloading data from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        print("\n--- File Contents ---")
        print(response.text)
        print("-----------------------\n")

        print("Successfully downloaded and displayed the file content.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading or processing the file: {e}")

if __name__ == "__main__":
    main()
