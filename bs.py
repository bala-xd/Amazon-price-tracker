import requests
from bs4 import BeautifulSoup
import lxml
import time


def get_data(url):
    user_agent = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Language': 'en'
    }
    page = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(page.text, 'lxml')
    name = soup.select_one(selector='#productTitle').text.strip()
    price = soup.select_one(selector='#priceblock_ourprice').text
    price = float(price[1:])
    return name, price
