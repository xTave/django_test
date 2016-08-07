from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QColor

from Gui.Base.widget import Widget


def set_painter_color(qp, args):
    qp.setPen(QColor(*args))
    qp.setBrush(QColor(*args))


def get_hbox(*args):
    hbox = QHBoxLayout()
    for i in args:
        hbox.addWidget(i)
    return hbox


class View:
    def __init__(self, widget: Widget):
        self.widget = widget
        self.configure_buttons()
        self.configure_labels()
        self.configure_widgets()
        self.set_layout()

    def set_layout(self):
        pass

    def configure_labels(self):
        pass

    def configure_buttons(self):
        pass

    def configure_widgets(self):
        pass