import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://www.mashina.kg'
URL = 'https://www.mashina.kg/search/all/'

def write_to_csv(data):
    with open("mashina.csv", 'a') as file1:
        writer = csv.writer(file1, delimiter=':')
        writer.writerow((data['title'],
                        data['price'],
                        data['opisanie'],
                        ))


def get_html(url, param=''):
    reques = requests.get(url, params=param)
    return reques
    

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='list-item list-label')

    for item in items:
        title = item.find('div', class_ = 'block title').get_text(strip = True),
        price = item.find('div', class_ = 'block price').find('strong').get_text(strip = True),
        opisanie = item.find('div', class_ = 'block info-wrapper item-info-wrapper').get_text(strip = True),

        data = {'title': title, 'price': price, 'opisanie': opisanie} 
        write_to_csv(data)

html = get_html(URL)
get_content(html.text)