# 07.12.2022

# род. класс
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points  = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def n(self):
        print(f'Wanted: {self.name}')

    def h(self):
        self.health_points *= 2

    def __str__(self):
        return f'Nickname: {self.nickname}' \
               f'Power: {self.superpower}' \
               f'Health: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Monkey D. Luffy', 'Mugiwarra\n', 'Gomu Gomu\n', 70, 'GomuGomuNoPISTOLET')
hero.n()
hero.h()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}')

# доч. 1класс
class MagnumHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        aceh = self.health_points ** 2
        self.health_points = aceh

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

ace = MagnumHero('Portgas D. Ace', 'Fire Fist\n', 'Mera Mera\n', 40, 'Dai Enkai Entei')
ace.h()
print(ace)
print(f'Damage: {ace.damage}')
ace.f()
print(f'Fly: {ace.fly}')
ace.phrase()


# доч. 2класс
class DestroyHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        dofih = self.health_points ** 2
        self.health_points = dofih

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

dofi = DestroyHero('Donquixote Doflamingo', 'Heavenly Yaksha\n', 'Ito Ito\n', 60, 'Tori Kago')
dofi.h()
print(dofi)
print(f'Damage: {dofi.damage}')
dofi.f()
print(f'Fly: {dofi.fly}')
dofi.phrase()

class Villain(DestroyHero):
    monster = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self):...

    def crit(self):
        print(f'Crit dm: {self ** 2}')

akainu = Villain('Sakazuki', 'Fleet Admiral\n', 'Magu Magu\n', 90, 'Ryusei Kazan')
print(akainu)
akainu.gen_x()
Villain.crit(ace.damage)