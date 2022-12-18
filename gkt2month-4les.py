# 15.12.2022
# геттеры, сеттеры
# множественное наследование

"""геттеры и сеттеры"""
class Emirlan:
    head = 1
    hands = 2
    foots = 2

    def __init__(self, name='Emirlan', age=18):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name}\n' \
               f'{self.__age}\n '

    @property
    def emirlan(self):
    # def get_emirlan(self):
        return f'{self.__name}, {self.__age}'

    @emirlan.setter
    def emirlan(self, name, age):
    # def set_emirlan(self, name, age):
        self.__name = name
        self.__age = age

    def run(self):
        self.__g()
        self._run()
        print(self.__age -1)
        print(self.__name)

    def _run(self):
        print(self.__name, 'run')

    def __g(self):
        pass

# e = Emirlan()
# e.run()
# print(e._Emirlan__name)
# amir = Emirlan('Emirlan', 0)
# amir._Emirlan__name = 'Amir'
# amir._Emirlan__age = 18
# print(amir.emirlan)
# amir.set_emirlan('Amir', 12)
# print(amir.get_emirlan())

"""множественное наследование"""
class One:

    def __init__(self, name):
        self.name = name

class Tho(One):

    def __init__(self, age):
        self.age = age

    def f(self):
        print('Амир молчит')

class Tho2(One):

    def f(self):
        print('Амир говорит')

    def tho2(self):
        print('эта функция Tho')

class Three(Tho2, Tho):

    def __init__(self, name, age):
        Tho.__init__(self, age)
        Tho2.__init__(self, name)

h = Three('Kuba', 99)
print(h)
# h.f()
# h.tho2()
