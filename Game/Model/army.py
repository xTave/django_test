from Model.functions import *


class Army:
    def __init__(self, units: list):
        self.units = units
        self.initiative = 0

    def update_initiative(self):
        self.initiative += sum(unit.initiative for unit in self.units)

    def get_initiative(self):
        return sum(unit.initiative for unit in self.units)

    def contains_units(self):
        return len(self.units) != 0

    def attack(self, other_army):
        i = get_rand_int(0, len(self.units) - 1)
        j = get_rand_int(0, len(other_army.units) - 1)
        self.units[i].attack(other_army.units[j])
        if other_army.units[j].health < 1:
            other_army.units.pop(j)