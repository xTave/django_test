from Model.functions import get_rand_int


class Weapon:
    def __init__(self, min_damage, max_damage):
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self):
        return get_rand_int(self.max_damage, self.max_damage)


class LazerWeapon(Weapon):
    def __init__(self):
        super().__init__(10, 15)


class PlasmaWeapon(Weapon):
    def __init__(self):
        super().__init__(15, 20)