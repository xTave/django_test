from PyQt5.QtGui import QPainter, QColor, QImage

from Gui.Base.widget import Widget
from Gui.NewGameMenu.ChooseStartWidget.choose_start_view import ChooseStartView
from Gui.NewGameMenu.ChooseStartWidget.choose_start_controller import ChooseStartController


class ChooseStartWidget(Widget):
    def __init__(self, population):
        self.population = population
        super().__init__(0, 0, 1, ChooseStartView, ChooseStartController)
        self.setFixedSize(600, 300)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, QImage("Files/2.png"))
        qp.end()
