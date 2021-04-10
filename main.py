import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QBoxLayout
from PyQt5.QtGui import QIcon
from win32api import GetSystemMetrics
from PyQt5.QtCore import QCoreApplication
import time

class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Face_Mask_Detector')
        self.resize(GetSystemMetrics(0) / 3 * 2, GetSystemMetrics(1) / 3 * 2)
        self.center()
        self.setWindowIcon(QIcon('python.png'))

            self.AddButton()
            self.show()


    def AddButton(self):
        btn = QPushButton('Push', self)
        btn.setGeometry(self.width() / 2, self.height() / 2, self.width() / 20, self.height() / 20)
        btn.clicked.connect(QCoreApplication.instance().quit)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())
