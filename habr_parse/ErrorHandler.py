from lxml.html import HTMLParser

class ErrorHandler:

    def _soup_error_handler(func):
        def wrapper(self, *args,  **kwargs):
            try:
                soup = func(self, *args, **kwargs)
                return soup
            except (SyntaxError, ImportError):
                print('SyntaxError, ImportError')
            except UnicodeEncodeError:
                print('UnicodeEncodeError')
        return wrapper


