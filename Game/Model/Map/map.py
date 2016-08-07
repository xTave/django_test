from Model.functions import *


class MapCell:
    def __init__(self, cell_type: str, trash_value: int, forest_value: int):
        self.trash_value = trash_value
        self.forest_value = forest_value
        self.type = cell_type


class Map:
    def __init__(self, seed: int, size: int):
        self.seed = seed
        self.cells = []
        self.cells_count = size
        self.generate()

    def generate(self):
        for i in range(self.cells_count * self.cells_count):
            forest = 0
            r = get_rand_int(0, 100)
            if r < 20:
                cell_type = "town"
            elif r > 90:
                cell_type = "sea"
            else:
                cell_type = "forest"

            if cell_type == "forest":
                trash = get_rand_int(0, 10)
                forest = get_rand_int(50, 100)
            elif cell_type == "sea":
                trash = 0
            else:
                trash = get_rand_int(50, 100)
            self.cells.append(MapCell(cell_type, trash, forest))

    def __getitem__(self, i):
        return self.cells[i[0] * self.cells_count + i[1]]



