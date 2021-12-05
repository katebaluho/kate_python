import typing
from datetime import datetime
from urllib.parse import urljoin
import bs4

# TODO: Логирование ошибок в БД
# Общая декомпозиция и универсализация подхода
# TODO: Предусмотреть повторный запуск без обхода дубликатов
from sqlalchemy.exc import IntegrityError

from ResponseMixin import ResponseMixin
from habr_parse.database import DB
from habr_parse.database import models
from habr_parse.ErrorHandler import ErrorHandler

db = DB()

class HabrParser(ResponseMixin):

    def __init__(self, start_url, delay=1.0):
        self.start_url = start_url
        self.done_urls = set()
        self.tasks = []
        self.tasks.append(self.get_task(self.start_url, self.rows_parse))
        #TODO: можно ли вынести это  в mixin??
        self._parse_time = 0
        self.delay = delay
        self.lin = []

    def get_task(self, url: str, callback: typing.Callable):
        def task():
            return callback(url)
        return task

    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            data = task()
            if data:
                self.save(data)


    def save(self, page_data):
        session = db.maker()

        author = models.Author(name = page_data['author_name'])
        session.add(author)
        session.commit()

        tags = [models.Tag(label=label) for label in page_data["tags"]]
        session.add_all(tags)

        publication = models.Publication(
                           title = page_data['title'],
                           create_date = page_data['create_date'],
                           url = page_data['url'],
                           author_id = author.id
        )

        for tag in tags:
            tag.publications.append(publication)
        session.add(publication)

        session.commit()
        session.close()


    @ErrorHandler._soup_error_handler
    def get_soup(self, url):
        response = self._get_response(url)
        soup = bs4.BeautifulSoup(response.text, "lxml")
        return soup


    def __links_parse(self, url, soup, class_name, callback):
        links = soup.find_all("a", attrs={"class": class_name})
        for itm in links:
            href = itm.attrs.get("href")
            if href:
                link = urljoin(url, href)
                if link not in self.done_urls:
                    self.done_urls.add(link)
                    self.tasks.append(self.get_task(link, callback))   #здесь вызываем и row, articles!!!! записываем таску


    def rows_parse(self, url):
        soup = self.get_soup(url)
        self.__links_parse(url, soup, "tm-pagination__page", self.rows_parse)
        self.__links_parse(url, soup, "tm-article-snippet__title-link", self.article_parse)
        print('url_rows_e',url)


    def article_parse(self, url):
        print('article_url', url)
        soup = self.get_soup(url)
        title = soup.find("h1", attrs={'class': 'tm-article-snippet__title'}).text
        create_date = datetime.fromisoformat(soup.find('time').attrs.get('datetime')[:-1])

        author_tag = soup.find('a', attrs={'class': "tm-user-info__username"})
        author_name = author_tag['href'].split('/')[-2]

        tags = [str(link.string) for link in soup.find_all('a', attrs={'class': 'tm-tags-list__link'})]

        return {'title' : title, 'create_date': create_date, 'url' : url, 'author_name' : author_name , 'tags': tags}


if __name__ == '__main__':
    start_url = "https://habr.com/ru/all/"
    parser = HabrParser(start_url, 0.2)
    parser.run()
