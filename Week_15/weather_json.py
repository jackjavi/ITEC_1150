"""
Author: Yusuf Hassan
Date: 2025-05-07
Description: This program reads weather forecast data from a JSON file
             and prints the forecast periods and detailed forecasts in two columns.
"""
import json

def main():
    filename = 'lab_16_forecast.json'

    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        forecast_periods = data.get('periods')

        if forecast_periods:
            max_period_len = max(len(item.get('name', '')) for item in forecast_periods) + 2
            for item in forecast_periods:
                period_name = item.get('name', '')
                detailed_forecast = item.get('detailedForecast', '')
                print(f"{period_name:<{max_period_len}}{detailed_forecast}")
        else:
            print(f"Error: No forecast data found under the 'periods' key in '{filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()