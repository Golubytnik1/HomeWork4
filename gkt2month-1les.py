# 05.12.2022

class Human:
    # атрибуты уровня класса
    head = 1
    body = 1

    # конструктор(функция def) - метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод
    def run(self):
        print(f'{self.name} is run')

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Возраст: {self.age}\n' \
               f'Тело: {self.head}\n'

hum = Human('Алдияр', 18)
hum.run()
hum.name = 'Максат'
print(hum)


class Raketa:
    toplivo = True
    kabina = 1
    korpus = 'ironMan'
    human = None
    def run(self, human):
        print(f'{human} is Fly')

Raketa.run(hum.name)