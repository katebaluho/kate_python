import requests
from urllib.parse import urljoin, urlparse
import pathlib
import re


"""
HTTP/s
HEADERS
BODY
status codes
- 1xx - Info
- 2xx - ОК, 201 Created
- 3xx - Redirect, 301 
- 4xx - 404 Ошибка пользователя
- 5xx - Server error
Методы запросов
- GET
- POST
- PUT
- PATCH
- DELETE
"""
headers = {
    "User-Agent": "Svetlana Loboda v.2",
}
# ?format[]=mm&format[]=ms&category[]=fruits_vegetables
params = {
    "format[]": ["mm", "ms"],
    "category[]": "fruits_vegetables",
}

# html_file_path = pathlib.Path(__file__).parent.joinpath("magnit_action.html")
print(1)
#
# with open(html_file_path, "wb") as file:
#     file.write(response.content)

pattern = re.compile(r"href=\"(/promo\S+)\"")


# a = re.findall()

def get_page(url, to_save=False):
    response = requests.get(url)
    if to_save:
        temporary = url.split("/")
        file_path = pathlib.Path(__file__).parent.joinpath(
            f"{temporary[-1] or temporary[-2]}.html"
        )
        with open(file_path, "wb") as file:
            file.write(response.content)
    return response


url = "https://magnit.ru/promo/"
response = get_page(url)

products = set()
for link in re.findall(pattern, response.text):
    base = urlparse(response.url)
    url = urljoin(response.url, link)
    if base.netloc == urlparse(url).netloc:
        if url not in products:
            _ = get_page(url, to_save=True)
        products.add(url)
print(1)


"""
ДЗ:
Написать программу, извлекающую данные
- Урл акции
- Название акции
и положить все в SQL БД (Посредством алхимии)
"""