import requests
from bs4 import BeautifulSoup


class GetPrice:
    """
    That class check price given item. It has 3 attributes, link to page where is a item, type of tag and class name
    """
    def __init__(self, url, tag, tag_name):
        self.url = url
        self.tag = tag
        self.tag_name = tag_name

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        accept_language = 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
        self.headers = {
            'User-Agent': user_agent,
            'Accept-Language': accept_language
        }

    def get_price(self) -> tuple[str, int]:
        response = requests.get(url=self.url, headers=self.headers)
        status = response.status_code
        soup = BeautifulSoup(response.text, 'lxml')
        whole_price = soup.find(name=self.tag, class_=self.tag_name)
        price = ''
        for digit in whole_price.text:
            if digit.isdigit():
                price += digit
        return price, status
