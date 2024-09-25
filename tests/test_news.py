import unittest

from news.news import get_news_rest_api

class TestNews(unittest.TestCase):

    def test_news_url(self):
        url = "www.some-url.com"
        news = get_news_rest_api(url)

        self.assertEqual(news, {})


if __name__ == '__main__':
    unittest.main()
