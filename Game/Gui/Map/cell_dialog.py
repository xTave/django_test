from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from Model.Map.map import MapCell


class CellDialog(QDialog):
    def __init__(self, cell: MapCell):
        super().__init__()
        self.buttons = [QPushButton("Ok")]
        self.labels = [QLabel(), QLabel(), QLabel()]
        self.cell = cell
        self.set_layout()
        self.setModal(True)
        self.connect_buttons()
        self.set_label_text()

    def set_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.labels[0])
        hbox = QHBoxLayout()
        hbox.addWidget(self.labels[1])
        hbox.addWidget(self.labels[2])
        vbox.addLayout(hbox)
        vbox.addStretch()
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.buttons[0])
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def connect_buttons(self):
        self.buttons[0].clicked.connect(self.accept)

    def set_label_text(self):
        self.labels[0].setText("{}".format(self.cell.type))
        self.labels[1].setText("Thrash: {}\nForest: {}".format(self.cell.trash_value, self.cell.forest_value))
        self.labels[2].setText("Ваши Войска: {}\nВойска Противника: {}".format(5, 0))