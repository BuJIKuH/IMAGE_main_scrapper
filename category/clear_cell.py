import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

def get_url():
    sleep(1)
    url = 'https://image-skincare.ru/category/buy-image-skincare'
    response = requests.get(url + '/clear-cell/', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all("div", class_="products-item")

    for all_data in data:
        card_url = 'https://image-skincare.ru' + all_data.find('a').get('href')
        yield card_url

def array_clear_cell():
    for card_descr in get_url():
        response = requests.get(card_descr, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('main', class_='main-content mobile-fixed')
        names = data.find('div', class_="product-name").text
        name = names.strip('\n')
        prices = data.find('div', class_='product-prices').text
        price = int(prices.replace('₽', '').strip('\n').strip().replace(' ', ''))
        descriptions = data.find('div', class_='description').text
        description = descriptions.strip('\n').strip()
        url_img = 'https://image-skincare.ru' + data.find('img').get('src')
        add_cards = data.find('div', class_="stocks").text
        add_card = add_cards.strip('\n')

        yield name, price, description, url_img, add_card





