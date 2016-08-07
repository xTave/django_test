from PyQt5.QtWidgets import QWidget, QLabel, QPushButton


class Widget(QWidget):
    def __init__(self, widgets_count, buttons_count, labels_count, view, controller):
        super().__init__()
        self.buttons = [QPushButton() for i in range(buttons_count)]
        self.labels = [QLabel() for i in range(labels_count)]
        self.widgets = [QWidget() for i in range(widgets_count)]
        self.view = view(self)
        self.controller = controller(self)