from urllib.parse import urljoin, urlparse
import pathlib
import re
from bs4 import BeautifulSoup as bs
from oop_web.models import PromoLink
from oop_web.data_base import DataBase
from oop_web.data_sourse import DataSourse

sourse = DataSourse()
db = DataBase()

def save_info(info):
    with open('info_log.txt', 'a') as file:
        file.write(info)


class DataParser:

    page = bs(sourse.response.text, 'html.parser')

    def get_all_promo_pages(self):
        promo_links = self.page.findAll('a', class_ = 'card-sale')
        if promo_links:
            return [link['href'] for link in promo_links]


    def get_label_promo_page(self, href_link):
        l = self.page.find('a', href = href_link)
        label = l.findChild('div', class_='card-sale__title')
        if label:
            return str(label.string)


    def get_promo_data(self):
        #можно было бы default dict , проверку на уникальность тоже не успеваю
        products_url = {}
        for link in self.get_all_promo_pages():
            base = urlparse(sourse.response.url)
            url = urljoin(sourse.response.url, link)
            if base.netloc == urlparse(url).netloc:
                # if url not in products_url.keys():
                # pass
                products_url[link] = self.get_label_promo_page(link)
        return products_url #можно сделать генератор



products = DataParser()


def fill_db():

    session = db.maker()
    for url_p, label_p in products.get_promo_data().items():
        session.add_all([
            PromoLink(url = url_p, label = label_p)
        ])
    session.commit()
    session.close()

fill_db()

print(1)