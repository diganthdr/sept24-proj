import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia Main Page
url = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract and print the title of the page
    page_title = soup.title.string
    print(f"Page Title: {page_title}")
    
    # Example: Extract all the headlines from the 'In the news' section
    in_the_news = soup.find('div', {'id': 'mp-itn'})
    headlines = in_the_news.find_all('li')
    
    print("\nHeadlines from 'In the news':")
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}. {headline.text}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
