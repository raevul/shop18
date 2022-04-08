# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://www.kivano.kg'

# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     pages = soup.find('ul', class_ = 'pagination pagination-sm')
#     last_page = pages.find_all('li')[-1]
#     total_page = last_page.find('a').text
#     return int(total_page)
    

# def write_to_csv_file(data):
#     with open('phones_kivano.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter=':')
#         writer.writerow((data['title'],
#                         data['price'],
#                         data['photo']))


# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     product_list = soup.find_all('div', class_ = 'list-view')
    
#     for product in product_list:
#         try:
#             photo = URL + product.find('div', class_ = 'listbox_img pull-left').find('img').get('src')
#         except:
#             photo = ''

#         try:
#             title = product.find('div', class_ = 'listbox_title oh').find('strong').text
#         except:
#             title = ''

#         try:
#             price = product.find('div', class_ = 'listbox_price text-center').find('strong').text
#         except:
#             price = ''

#         data = {'title': title, 'price': price, 'photo': photo}

# def main():
#     photos_url = 'https://www.kivano.kg/mobilnye-telefony'
#     pages = '?page='
#     total_pages = get_total_pages(get_html(photos_url))
#     print(total_pages)
#     for page in range(1, 32):
#         url_with_page = photos_url + pages + str(page)
#         print(url_with_page)
    
# main()





import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://www.kivano.kg'

def get_html(url):
    response = requests.get(url)
    return response.text


def get_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('ul', class_ = 'pagination pagination-sm')
    last_page = pages.find_all('li')[-1]
    total_page = last_page.find('a').text
    return int(total_page)


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    phones_list = soup.find('div', class_ = 'list-view')

    # for phone in phones_list:
    title = phones_list.find('div', class_ ='item product_listbox oh')
    print(title)
        # price = phone.find('div', class_ = 'listbox_price text-center').text
        # photo = URL + phone.find('div', class_ = 'listbox_img pull-left').find('img').get('src')

        # data = {'title': title, 'price': price, 'photo': photo}
        

def main():
    phones_url = 'https://www.kivano.kg/mobilnye-telefony'
    pages = '?page='
    get_pages(get_html(phones_url))
    get_page_data(get_html(phones_url))
    
main()
