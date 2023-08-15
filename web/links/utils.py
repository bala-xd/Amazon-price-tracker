import requests
from bs4 import BeautifulSoup
import lxml
import time


def get_data(url):
    user_agent = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Language': 'en'
    }

    #page = requests.get(url, headers=user_agent)

    with open(url+'.html', 'r', encoding='utf-8') as f:
      page = f.read()
    soup = BeautifulSoup(page, 'lxml')
    name = soup.select_one(selector='#productTitle').text.strip()
    price = soup.find('span', class_='a-price-whole').text.strip().replace(',', '')
    price = float(price)
    return name, price

#print(get_data(''))