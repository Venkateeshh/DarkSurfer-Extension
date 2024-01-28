import requests
from bs4 import BeautifulSoup

def get_webpage_source(url):
    try:
        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Get the source code of the webpage
            source_code = str(soup)

            return source_code
        else:
            print(f"Error: Unable to fetch the webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input the URL of the webpage
    url = input("Enter the URL of the webpage: ")

    # Get the source code of the webpage
    webpage_source = get_webpage_source(url)

    if webpage_source:
        # Print the source code (or you can save it to a file, etc.)
        print(webpage_source)
