from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from widgets import windowTrain_ui as ui
import random , time

class windowTrainClass(QDialog, ui.Ui_WindowTrain):
    def __init__(self,words):
        super(windowTrainClass,self).__init__()
        self.setupUi(self)
        self.words = words
        self.word = random.choice(list(self.words.keys()))

        #timer
        self.interval = 500
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateUpWord)
        self.timer.start(self.interval)

        self.translationTimer = QTimer()
        self.translationTimer.timeout.connect(self.updateDownWord)

    def updateUpWord(self):
        self.newWord = random.choice(list(self.words.keys()))
        while self.newWord == self.word:
            self.newWord = random.choice(list(self.words.keys()))
            print(self.newWord,self.word)
        self.word = self.newWord
        self.transl = self.words[self.word]

        self.wordUp_lb.setText(self.word)
        self.wordDown_lb.setText('')
        self.timer.stop()
        self.translationTimer.start(3000)

    def updateDownWord(self):
        self.wordDown_lb.setText(self.transl)
        self.translationTimer.stop()
        self.timer.start(1000)


if __name__ == '__main__':
    app = QApplication([])
    w = windowTrainClass({'he': 'он', 'it ': 'оно', 'we': 'мы'})
    w.show()
    app.exec()