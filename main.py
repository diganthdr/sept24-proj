
from news.news import get_news_rest_api
from notify.sendemail import sendemail
# driver code
def main():
    news = get_news_rest_api(url)
    # weather = 
    # movies

    for subscriber in subscribers:
        sendemail()