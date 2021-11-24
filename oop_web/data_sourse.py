import requests

URL_SOURSE = "https://magnit.ru/promo/"


class DataSourse:

    url = URL_SOURSE

    params = {
        "format[]": ["mm", "ms"],
        "category[]": "bakaleya",
    }

    def __init__(self):
        response = self.get_response()

    def get_response(self):
        self.response = requests.get(self.url)

