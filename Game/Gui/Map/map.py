from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QKeyEvent

from Model.Map.map import MapCell, Map

from Gui.Map.cell_dialog import CellDialog


class MapCellGui(QWidget):
    def __init__(self, cell: MapCell):
        super().__init__()
        self.cell = cell
        self.cell_size = 100
        self.setFixedSize(self.cell_size, self.cell_size)

    def paintEvent(self, QPaintEvent):
        qp = QPainter()

        def change_color(args):
            qp.setPen(QColor(*args))
            qp.setBrush(QColor(*args))

        qp.begin(self)
        if self.cell.type == "forest":
            change_color((0, 255, 0))
        elif self.cell.type == "sea":
            change_color((0, 0, 255))
        else:
            change_color((255, 0, 0))
        qp.drawRect(0, 0, self.cell_size, self.cell_size)
        change_color((0, 0, 0))
        qp.drawText(10, 15, "Trash: {}".format(self.cell.trash_value))
        qp.drawText(10, 30, "Forest: {}".format(self.cell.forest_value))
        qp.end()

    def mousePressEvent(self, QMouseEvent):
        CellDialog(self.cell).exec()


class MapGui(QWidget):
    def __init__(self, map: Map):
        super().__init__()
        self.map = map
        self.cells_count = 9
        self.cells = []
        self.shift_i = 0
        self.shift_j = 0
        self.set_layout()
        self.setFixedSize(self.cells_count * 100, self.cells_count * 100)

    def set_layout(self):
        grid = QGridLayout()
        for i in range(self.cells_count):
            for j in range(self.cells_count):
                self.cells.append(MapCellGui(self.map[i, j]))
                grid.addWidget(self.cells[-1], i, j)
        grid.setSpacing(0)
        self.setLayout(grid)

    def keyPressEvent(self, e):
        e = QKeyEvent(e)
        print(e.key())
        if e.key() == 83:
            self.shift_i += 1
        if e.key() == 87:
            self.shift_i -= 1
        if e.key() == 68:
            self.shift_j += 1
        if e.key() == 65:
            self.shift_j -= 1
        if self.shift_i < 0:
            self.shift_i = 0
            return
        if self.shift_i > self.map.cells_count - self.cells_count:
            self.shift_i = self.map.cells_count - self.cells_count
            return
        if self.shift_j < 0:
            self.shift_j = 0
            return
        if self.shift_j > self.map.cells_count - self.cells_count:
            self.shift_j = self.map.cells_count - self.cells_count
            return
        for i in range(self.cells_count):
            for j in range(self.cells_count):
                    self.cells[self.cells_count * i + j].cell = self.map[i + self.shift_i, j + self.shift_j]
                    self.cells[self.cells_count * i + j].update()