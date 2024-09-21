from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class testClass(QDialog):
    def __init__(self):
        super(testClass,self).__init__()
        self.resize(600,500)

        ly = QHBoxLayout(self)

        rad = QRadioButton()
        ly.addWidget(rad)

        self.text1 = QLabel('text')
        ly.addWidget(self.text1)

        self.text2 = QLabel('text')
        ly.addWidget(self.text2)



if __name__ == '__main__':
    app = QApplication([])
    w = testClass()
    w.show()
    app.exec()
