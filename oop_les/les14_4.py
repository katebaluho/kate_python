import os
from os import path


class SomeDecorator:

    def __init__(self, obj):
        self.obj = obj
        self.instance = None

    def __call__(self, *args, **kwargs):
        self.instance = self.obj(*args, **kwargs)
        return self

    def __getattr__(self, name):
        print(f"Вызван метод {name}")
        return getattr(self.instance, name)

    # @classmethod
    # def all_decorators(cls, obj):
    #     return cls(obj)
    #


import datetime


class Logger:

    def __init__(self, func, file_path):
        self.func = func
        self.file_path = file_path

    def __call__(self, *args, **kwargs):
        self.__log()
        return self.func(*args, **kwargs)

    def __log(self):
        with open(self.file_path, "a", encoding="UTF-8") as file:
            file.write(f"{datetime.datetime.now()}: {self.func.__name__}")

    @classmethod
    def to_file(cls, file_path):
        return lambda func: cls(func, file_path)


@Logger.to_file(path.join(path.dirname(__file__), "log1.txt"))
def my_func(a, b):
    return a + b


@Logger.to_file(path.join(path.dirname(__file__), "log2.txt"))
def my_func2(a, b, c):
    return sum((a, b, c))


@SomeDecorator
class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say(self):
        print(f"my name is {self.name} {self.surname}")


# human = Human("Sergey", "Romanchuk")
print(my_func(2, 3))
print(my_func2(2, 3, 4))
print(1)
