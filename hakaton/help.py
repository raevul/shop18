import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://www.mashina.kg'
HOST = 'https://www.mashina.kg/search/all/'
CSV = 'mashina.csv'

def get_html(url):
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    html = requests.get(url)
    return html.text


# def get_pages(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     pages = soup.find('ul', class_ = 'pagination')
#     last_page = pages.find_all('li')[-4]
#     total_page = last_page.find('a').text
#     return int(total_page)


def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    cars_list = soup.find_all('div', {'class': 'list-item list-label'})
    new_list = []

    for cars in cars_list:
        new_list.append(
            {
                'title': cars.find('div', class_ = 'block title').get_text(strip = True),
                'price': cars.find('div', class_ = 'block price').find('strong').get_text(strip = True),
                'opisanie': cars.find('div', class_ = 'block info-wrapper item-info-wrapper').get_text(strip = True)
            })
        return new_list


response = requests.get(URL)
def save(response,path):
    with open(path, 'a') as file: 
        writer = csv.writer(file, delimiter =';')
        writer.writerow(['название',"цена","описание","фотки"]) # Указываем название столбцов
        for i in response:
            writer.writerow([i['title'],i['price'],i['opisanie']]) # Записываем наши данные 

            # writer.writerow([i['title'],i['price'],i['opisanie'],i['images']]) # Записываем наши данные 

save(get_total_pages(response.text),CSV)


# def main():
#     cars_url = 'https://www.mashina.kg/search/all/'
#     pages = '?page='
#     get_pages(get_html(cars_url))

# main()