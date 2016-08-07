from Gui.Base.view import View, get_hbox


class ChooseStartView(View):
    def set_layout(self):
        hbox = get_hbox(*self.widget.labels)
        self.widget.setLayout(hbox)

    def configure_labels(self):
        self.widget.labels[0].setText("qwertyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq\nasdfg\nzxcvb"
                                      "\n\n\n\n\n\n123")