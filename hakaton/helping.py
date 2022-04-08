import requests
from bs4 import BeautifulSoup
import csv
CSV = 'phone_kivano.csv'
HOST = 'https://www.kivano.kg'
URL = 'https://www.kivano.kg/mobilnye-telefony'

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser') 
    items = soup.find_all('div', class_ = 'item product_listbox oh')
    phones = []

    for item in items:
        phones.append({
            'title': item.find('div', class_ = 'product_text pull-left').find('div', class_ = 'listbox_title oh').find('a').get_text(strip = True),
            'price': item.find('div', class_ = 'motive_box pull-right').find('div', class_ = 'listbox_price text-center').get_text(strip = True),
            'nalichie': item.find('div', class_ = 'motive_box pull-right').find('div', class_ = 'listbox_motive text-center').get_text(strip = True),
            'images': HOST + item.find('div', class_='listbox_img pull-left').find('img').get('src') 
        })
    return phones

response = requests.get(URL)
def save(response,path):
    with open(path, 'a') as file: 
        writer = csv.writer(file, delimiter =';')
        writer.writerow(['название',"цена","наличие","фотки"])
        for items in response:
            writer.writerow([items['title'],items['price'],items['nalichie'],items['images']])

save(get_content(response.text),CSV)