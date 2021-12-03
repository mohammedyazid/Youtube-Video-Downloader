from PyQt5.QtWidgets import QMainWindow,QApplication
from Methods import methods
from Ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SUBMIT.clicked.connect(lambda:methods.submitc(methods))
        self.ui.DOWNLOAD.clicked.connect(lambda:methods.downloadc(methods))
        self.ui.path_button.clicked.connect(lambda:methods.topath(methods))
        self.ui.url_button.clicked.connect(lambda:methods.clear(methods))
if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        sys.exit(app.exec())