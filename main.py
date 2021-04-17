import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDesktopWidget
import PyQt5
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

        image = QPixmap("teemo minimalistic.jpg")

        lbl_img = QLabel()
        lbl_img.setPixmap(image)
        lbl_size = QLabel('Width: ' + str(image.width()) + ', Height: ' + str(image.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)

        self.PUSHBUTTON("PUSH BUTTON", True, vbox)

        self.setLayout(vbox)

        self.showMaximized()

    def PUSHBUTTON(self, title, bl, vbox):
        btn = QPushButton(title, self)
        btn.setEnabled(bl)
        vbox.addWidget(btn)

    def CENTER(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = APP()
    sys.exit(app.exec_())