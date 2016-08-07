from Model.functions import get_rand_int


class Unit:
    def __init__(self, health, initiative, armor, weapon):
        self.max_health = get_rand_int(*health)
        self.weapon = weapon
        self.armor = armor
        self.health = self.max_health + self.armor.bonus_health
        self.initiative = get_rand_int(*initiative) + self.armor.bonus_initiative

    def attack(self, other_unit):
        other_unit.get_damage(self.weapon.get_damage())

    def get_damage(self, damage):
        self.health -= damage - self.armor.protection