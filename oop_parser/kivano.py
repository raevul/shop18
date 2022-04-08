from base_parser import BaseParser

class KivanoParser(BaseParser):
    # pass
    def get_links_data(self):
        html = self.get(kivano.base_url + '/elektronika')
        soup =self.init_soup(html)
        return soup.find('h1')
    

kivano = KivanoParser('https://kivano.kg')
# res = kivano.get(kivano.base_url + "/elektronika")
res = kivano.get_links_data()
print(res)