from Model.armor import *
from Model.army import Army
from Model.weapon import *

from Model.units import Unit


class Battle:
    def __init__(self, army1: Army, army2: Army):
        self.army1 = army1
        self.army2 = army2

    def begin(self):
        self.army1.update_initiative()
        self.army2.update_initiative()
        while self.army1.contains_units() and self.army2.contains_units():
            if self.army1.initiative > self.army2.initiative:
                self.army1.attack(self.army2)
                self.army2.update_initiative()
            else:
                self.army2.attack(self.army1)
                self.army1.update_initiative()
        if self.army1.contains_units():
            print(1, len(self.army1.units))
        else:
            print(2, len(self.army2.units))

for q in range(10):
    army1 = Army([Unit((16, 22), (10, 14), HeavyArmor(), PlasmaWeapon()) for i in range(1000)])
    army2 = Army([Unit((16, 22), (12, 14), TacticalArmor(), PlasmaWeapon()) for j in range(980)])
    Battle(army1, army2).begin()