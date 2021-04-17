import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class APP(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Face Mask Detector")
        self.setGeometry(300, 300, 300, 300)
        self.CENTER()

        # value
        self.number = 1

        # image
        div = 10
        self.image1 = QPixmap("teemo.jpg")
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.image1)
        self.lbl_img.setAlignment(Qt.AlignCenter)

        self.image2 = QPixmap("teemo.png")

        # push button
        btn1 = QPushButton("change picture", self)
        btn1.setEnabled(True)

        # label
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lbl_img)
        self.vbox.addWidget(btn1)

        self.setLayout(self.vbox)

        # event
        btn1.clicked.connect(self.CHANGE)

        self.showMaximized()

    def CENTER(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def CHANGE(self):
        if self.number is 1:
            self.number = 2
            self.lbl_img.setPixmap(self.image2)

        else:
            self.number = 1
            self.lbl_img.setPixmap(self.image1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = APP()
    sys.exit(app.exec_())