from abc import ABC, abstractmethod

class Hero(ABC):
    # @abstractmethod
    # def ulti(self):
    #     pass


    def __init__(self,name,health,attack,armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor


    def hitung_damage(self,target):
        return max(self.attack - target.armor, 0)

    def serang(self,target):
        damage = self.hitung_damage(target)
        target.health -= damage
        print(f'{self.name} menyerang {target.name}, damage {damage}')
#102
    #magic method
    def __add__(self,other):
        return self.attack + other.attack

    def __gt__(self,other):
        return self.attack > other.attack

class Mage(Hero):
    def hitung_damage(self,target):
        return self.attack

    def ulti(self):
        print(f"{self.name} melakukan ulti")

    def __str__(self):
        return f'namaku {self.name}'

class Warrior(Hero):
    def ulti(self):
        pass

class Minion():
    def __init__(self,name,health,armor=2):
        self.name = name
        self.health = health
        self.armor = armor

balmon = Warrior('balmon',100,15,4)
chou = Hero('chou',100,2,4)
eudora = Mage('eudora',80,5,2)

minion = Minion('minion',50,2,)

#91,103,102
# print(isinstance(eudora,Hero))
# print(isinstance(chou,Hero))
print(type(eudora))

"""
type
isintance()
"""
# print(eudora)
# print(balmon > eudora)
# print(eudora.attack + balmon.attack)
# balmon.serang(minion)
# eudora.serang(minion)