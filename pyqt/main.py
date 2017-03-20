import sys
import MainDialog
from PyQt5.QtWidgets import QApplication
if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MainDialog.MainDialog()
    m.show()
    app.exec_()