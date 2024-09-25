# This module gets news from various sources
# interface : get_news

import requests
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


# Basic configuration for logging
logging.basicConfig(level=logging.DEBUG)

# Logging messages

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")




url = "https://newsapi.org/v2/everything?q=apple&from=2024-09-19&to=2024-09-19&sortBy=popularity&apiKey=1806c703188d4b5da65aa1120ae7b49c"
url = "www.nonexists-23.com"

def get_news_rest_api(api):
    # Scrape news from API
   
   # if not validateurl(url):
    #    return False
    news = {}
    logging.info("Getting news from API")
    try:
        response = requests.get(url=api)

        if response.status_code != 200:
            logging.fatal(" Could not get OK response")
            return False

        articles = response.json()['articles']

        for article in articles:
            print("- ", article['title'])
            news.update(
            {article['title']:article['description']}
            )

    except Exception as e:
        logging.error(" Could not get OK response")

    return news

def get_news():
    news_json = get_news_rest_api()
    return news_json

if __name__ == '__main__':
    get_news_rest_api(url)
