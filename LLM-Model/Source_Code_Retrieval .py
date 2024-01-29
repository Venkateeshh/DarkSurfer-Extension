import requests
from bs4 import BeautifulSoup

def get_webpage_source(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            source_code = str(soup)

            return source_code
        else:
            print(f"Error: Unable to fetch the webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the webpage: ")

    webpage_source = get_webpage_source(url)

    if webpage_source:
        print(webpage_source)
