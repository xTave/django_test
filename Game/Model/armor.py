class Armor:
    def __init__(self):
        self.protection = 0
        self.bonus_health = 0
        self.bonus_initiative = 0

class TacticalArmor:
    def __init__(self):
        self.protection = 1
        self.bonus_health = 1
        self.bonus_initiative = 2


class HeavyArmor:
    def __init__(self):
        self.protection = 4
        self.bonus_health = 5
        self.bonus_initiative = -2