# 12.12.2022
# git clone
# инкапсуляция

class Emirlan:
    head = 1
    hands = 2
    foots = 2

    def __init__(self, name='Emirlan', age=18):
        self.__name = name
        self._age = age

    def __str__(self):
        return f'{self.__name}\n' \
               f'{self._age}\n '

    def run(self):
        self.__g()
        self._run()
        print(self._age -1)
        print(self.__name)

    def _run(self):
        print(self.__name, 'run')

    def __g(self):
        pass

e = Emirlan()
e.run()
print(e._Emirlan__name)
# e.__name = 'Амир'
# print(e.__name)