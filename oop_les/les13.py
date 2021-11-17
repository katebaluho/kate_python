import random

from oop_1.mixins import PainMixin


class Bio:

    def __init__(self):
        self.dnk = random.randint(10 ** 2, 10 ** 5)


class Bactery(Bio):

    def __init__(self):
        self.eat = random.choice(("O", "C", "H"))
        super().__init__()


class Reptile(Bactery):

    def __init__(self):
        self.brain = random.choice((True, False))
        super().__init__()

    def say(self):
        say_str = "HELLO" if self.brain else "hgfjhgffhlwherfgsgsh"
        print(say_str)


class UFO(Bio):
    name = None

    def say(self):
        print(f"Меня зовут {self.name}")


class Human(UFO):

    def __init__(self):
        self.name = random.choice(("R2d2", "Bill", "Obi Wan", "Weidar"))
        super().__init__()


class Gibrid(Human, Reptile, PainMixin):

    def say(self):
        print("ЧТО Я ТАКОЕ?")
        super().say()


gibrid = Gibrid()
print(1)
