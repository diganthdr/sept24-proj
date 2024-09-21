# This module gets news from various sources
# interface : get_news

def get_news_rest_api(api):
    return news 

def get_news():
    news_json = get_news_rest_api()
    return news_json

url = "https://newsapi.org/v2/everything?q=apple&from=2024-09-19&to=2024-09-19&sortBy=popularity&apiKey=1806c703188d4b5da65aa1120ae7b49c"
import requests
response = requests.get(url=url)
articles = response.json()['articles']
list_of_news = {}
for article in articles:
    print("- ", article['title'])
    list_of_news.update(
    {article['title']:article['description']}
    )

import pandas as pd

# Sample dictionary with single values
data = list_of_news

# Convert dictionary to DataFrame
df = pd.DataFrame(list(data.items()), columns=['Key', 'Value'])
breakpoint()
# Export DataFrame to Excel
df.to_excel('output_file.xlsx', index=False)

print("Data exported to Excel successfully.")
