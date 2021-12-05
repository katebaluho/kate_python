import time
import requests

RETRY_STEP = 3

class ResponseMixin:

    '''
    In the event of a network problem (e.g. DNS failure, refused connection, etc), Requests will raise a ConnectionError exception.
    In the event of the rare invalid HTTP response, Requests will raise an HTTPError exception.
    If a request times out, a Timeout exception is raised.
    If a request exceeds the configured number of maximum redirections, a TooManyRedirects exception is raised.
    All exceptions that Requests explicitly raises inherit from requests.exceptions.RequestException.
    '''

    #  Ретрай при недоступности с контролем количества
    # Предусмотреть количество плохих повторений циклов
    # TODO: сделать здесь лог ошибок

    def _retry_response(func):
        def wrapper(self, *args, **kwargs):
            retry_step = RETRY_STEP
            while retry_step != 0:
                try:
                    response = func(self, *args, **kwargs)
                    print('Response status code ',response.status_code)
                    response.raise_for_status()
                    return response
                except requests.exceptions.HTTPError :
                    print('HTTPError')
                except requests.exceptions.Timeout:
                    print('Timeout error')
                except requests.exceptions.TooManyRedirects:
                    print('TooManyRedirects')
                except requests.exceptions.RequestException :
                    print('catastrofic')
                retry_step -= 1
            print('Fail to get response')
            raise SystemExit(0)
        return wrapper


    @_retry_response
    def _get_response(self, url):
        while True:
            next_time = self._parse_time + self.delay
            now_time = time.time()
            if next_time > now_time:
                time.sleep(next_time - now_time)
            response = requests.get(url)
            self.__parse_time = now_time
            return response
