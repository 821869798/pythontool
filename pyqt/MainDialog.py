from PyQt5.QtWidgets import QDialog
from Ui_MainDialog import Ui_MainDialog
class MainDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui = Ui_MainDialog()
        ui.setupUi(self)
        self.ui = ui
        self.ui.button.clicked.connect(self.button_clicked)
        self.setFixedSize(self.frameSize())

    def button_clicked(self):
        text = self.ui.lineEdit.text()
        if text:
            self.ui.label.setText(text)