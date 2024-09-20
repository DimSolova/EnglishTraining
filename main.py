from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widgets import mainWindow_ui as ui
import setting, tableDictinary,trainingSetting

class MianWindowClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(MianWindowClass,self).__init__()
        self.setupUi(self)
        self.stt = setting.setting()
        self.dict = self.stt.get_dictanory()

        #connect
        self.words_btn.clicked.connect(self.openWords)
        self.train_btn.clicked.connect(self.openTrainSet)

    def openWords(self):
        self.vocab = tableDictinary.TableDialogDict()
        self.vocab.exec()
        data = self.vocab.saveTable()
        self.stt.add_words(data)

    def openTrainSet(self):
        self.train = trainingSetting.TrainingSettingClass()
        self.train.exec()








if __name__ == '__main__':
    app = QApplication([])
    w = MianWindowClass()
    w.show()
    app.exec()

