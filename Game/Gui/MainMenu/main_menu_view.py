from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from DB.main import DataBaseIdEnum, DataBaseWidgetTypeEnum, get_widgets_text
from Gui.Base.view import View, get_hbox


class MainMenuView(View):
    def set_layout(self):
        vbox = QVBoxLayout()
        for i in self.widget.labels:
            vbox.addLayout(get_hbox(i))
        for i in self.widget.buttons:
            vbox.addLayout(get_hbox(i))
        self.widget.setLayout(vbox)

    def configure_labels(self):
        def set_label(i, alignment, pixel_size, text):
            font = QFont()
            font.setPixelSize(pixel_size)
            self.widget.labels[i].setAlignment(alignment)
            self.widget.labels[i].setFont(font)
            self.widget.labels[i].setText(text)

        texts = get_widgets_text(DataBaseIdEnum.MainMenu, DataBaseWidgetTypeEnum.Labels)
        set_label(0, Qt.AlignCenter, 50, next(texts))
        set_label(1, Qt.AlignRight, 20, next(texts))

    def configure_buttons(self):
        texts = get_widgets_text(DataBaseIdEnum.MainMenu, DataBaseWidgetTypeEnum.Button)
        for i in self.widget.buttons:
            i.setMaximumHeight(1000)
        for i in range(len(self.widget.buttons)):
            self.widget.buttons[i].setText(next(texts))