from PyQt5.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setCentralWidget(widget)
        self.show()


WINDOW = object()


def create_window(widget):
    global WINDOW
    WINDOW = Window(widget)
    WINDOW.show()


def set_central_widget(widget):
    WINDOW.setCentralWidget(widget)
    WINDOW.keyPressEvent = widget.keyPressEvent