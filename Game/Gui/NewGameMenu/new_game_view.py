from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from Gui.Base.view import View, get_hbox
from Gui.NewGameMenu.ChooseStartWidget.choose_start_widget import ChooseStartWidget


class NewGameView(View):
    def set_layout(self):
        vbox = QVBoxLayout()
        q = 0
        for i in range(len(self.widget.widgets)):
            vbox.addLayout(get_hbox(*self.widget.widgets[q:q + 2]))
            q += 2
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.widget.buttons[0])
        vbox.addLayout(hbox)
        self.widget.setLayout(vbox)

    def configure_widgets(self):
        self.widget.widgets = [ChooseStartWidget(i) for i in range(len(self.widget.widgets))]