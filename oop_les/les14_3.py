from abc import ABC, abstractmethod


class SomePeople(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def say(data: str) -> None:
        pass


class Person(SomePeople):
    name = "SOME"

    def __init__(self):
        pass
        # self.name = "SOME"

    def get_name(self) -> str:
        return self.name

    @staticmethod
    def say(data: str) -> None:
        print(data)


human = Person()
print(human.get_name())
human.say("hello")