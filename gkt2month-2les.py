# 08.12.2022
# наследование, полиморфизм

# родительский класс
class Bot:
    brain = True

    def __init__(self, name, model, color, destination):
        self.name = name
        self.model = model
        self.color = color
        self.destination = destination

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Model: {self.model}\n' \
               f'Color: {self.color}\n'

    def destiny(self):
        print(f'Destiny: {self.destination}')

robot = Bot('Kuba', 'M1', 'pink', 'ebat mozgi')
print(robot)
print(robot.destiny())


# дочерний класс
class Robot(Bot):
    brain = False

    def __init__(self, name, model, color, destination, fly):
        super().__init__(name, model, color, destination)
        Bot.__init__(self, name, model, color, destination)
        self.fly = fly

    def destiny(self):
        self.fly = False
        print(self.fly)

robot2 = Robot('Terminal', 'T1001', 'orange', 'destroy', True)
print(robot2.fly)
robot2.destiny()
print(robot2.fly)
print(robot2.brain, robot.brain)

class Terminal(Robot):

    def destiny(self):
        print(self, 'теперь он летает')

robot3 = Terminal('Mbank', 'bankomat', 'green', 'give money', False)
robot3.destiny()

class Human:
    head = 1
    body = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is run')

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Возраст: {self.age}\n' \
               f'Тело: {self.head}\n'

hum = Human('Алдияр', 18)
Terminal.destiny(hum.name)