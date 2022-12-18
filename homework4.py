# 18.12.2022

class Name:

    def __init__(self, name):
        self.name = name

class Age:

    def __init__(self, age):
        self.age = age

class Animal:

    def _run(self):
        animal = 'собака'
        print(f'Ваш домашний питомец: {animal}')

class Math:

    def __mul__(self):
        a = 2
        b = 8
        result = a * b
        print(f'Ответ: {result}')

class Print(Name, Age, Animal, Math):

    def __init__(self, name, age):
        Name.__init__(self, name)
        Age.__init__(self, age)

    def __str__(self):
        return f'Ваше имя: {self.name}\n' \
               f'Ваш возраст: {self.age}'


last = Print('Amir', 17)
print(last)
last._run()
last.__mul__()