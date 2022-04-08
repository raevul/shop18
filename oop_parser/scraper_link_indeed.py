from base_parser import BaseParser

# super - обращается к родительскому классу и вызывает тот класс
# super -> BaseParser

class IndeedLinkParser(BaseParser):
    def __init__(self, base_url, name_of_parser):
        super().__init__(base_url)
        self.name_of_parser = name_of_parser

link_parser = IndeedLinkParser('https://www.indeed.com', 'Link Parser')
res = link_parser.get('https://www.indeed.com/jobs?q=python%20developer&l=New%20York%2C%20NY&vjk=1bd39d1f5f9094ba')
print(res)
