import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.elitebrainsconsulting.com/research")
# response = requests.get("https://automatetheboringstuff.com/2e/chapter12")
# print(response.status_code == requests.codes['OK'])  # Check if the request was successful
# print(response.raise_for_status())  # Raise an error for bad responses
# print(len(response.text))  # Print the length of the response text
# print(response.text)

parser = BeautifulSoup(response.text, 'html.parser')
programs = parser.select('h1, h2, h3, h4, h5, h6')  # Select all header tags
for program in programs:
  print('---------------')
  print(program.text)