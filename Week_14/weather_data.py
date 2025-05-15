"""
Author: Yusuf Hassan
Date: 2025-04-29
Description: This program accepts a Weather forecast Service URL,
             downloads the page, extracts the time periods and weather
             conditions, and displays them in two columns. It handles
             download errors and cases where no forecast data is found.
"""
import requests
from bs4 import BeautifulSoup as soup
import pyinputplus as pyip

def get_weather_data(url):
    """Downloads and parses weather forecast data from the given URL."""
    try:
        print(f"Downloading weather forecast data from: {url}")
        response = requests.get(url)
        response.raise_for_status()
        page_soup = soup(response.text, 'html.parser')
        time_periods = page_soup.select('.forecast-label')
        weather_conditions = page_soup.select('.forecast-text')
        return [period.get_text() for period in time_periods], [condition.get_text() for condition in weather_conditions]
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the page: {e}")
        return None, None

def display_forecast(periods, conditions):
    """Displays the time periods and weather conditions in two columns."""
    if not periods or not conditions:
        print("No forecast data found on the page.")
        return

    print("\n--- Weather Forecast ---")
    max_len = max(len(period) for period in periods) + 2  # Adjust spacing
    for i in range(min(len(periods), len(conditions))):
        print(f"{periods[i]:<{max_len}}{conditions[i]}")
    print("------------------------\n")

def main():
    """Main function to get URL, fetch data, and display the forecast."""
    while True:
        forecast_url = pyip.inputURL(prompt="Please enter the URL for your Weather forecast: ")
        time_periods, weather_conditions = get_weather_data(forecast_url)

        if time_periods is not None and weather_conditions is not None:
            if not time_periods or not weather_conditions:
                print("No forecast data found at the provided URL. Please try again.")
                continue
            else:
                display_forecast(time_periods, weather_conditions)
                break
        else:
            print("There was a problem downloading the page. Please try again.")

if __name__ == "__main__":
    main()