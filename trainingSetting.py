from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from widgets import trainingSetting_ui as ui
import setting
import windowTrain

class TrainingSettingClass(QDialog,ui.Ui_TrainingSetting):
    def __init__(self):
        super(TrainingSettingClass,self).__init__()
        self.setupUi(self)
        self.stt = setting.setting()
        self.radioList = []

        #connect
        self.start_btn.clicked.connect(self.startTrain)

        #start
        self.fillList()

    def fillList(self):
        data = self.stt.get_dictanory()
        if data:
            for k, v in data.items():
                customWidget = QWidget()
                layout = QHBoxLayout()
                radio = QRadioButton()
                radio.setChecked(True)
                radio.setMaximumWidth(20)
                layout.addWidget(radio)
                self.radioList.append(radio)
                word = QLabel(f"{k}")
                word.setMaximumWidth(300)
                layout.addWidget(word)
                transl = QLabel(f"{v}")
                layout.addWidget(transl)
                customWidget.setLayout(layout)  # Set the layout for the custom widget
                layout.setContentsMargins(0,0,50,0)
                listWidgetItem = QListWidgetItem()
                listWidgetItem.setSizeHint(customWidget.sizeHint())  # Set the size hint for proper display
                self.listWords_lw.addItem(listWidgetItem)  # Add the encapsulated custom widget
                self.listWords_lw.setItemWidget(listWidgetItem, customWidget)  # Set the custom widget for the item

    def startTrain(self):
        words = self.isChecked()
        if words:
            if self.selectLang_cb.currentText() == 'Russian - English':
                words = self.swap(words)
            if not self.showAnsw_cb.isChecked():
                words = self.cleanValue(words)
            self.windTrain = windowTrain.windowTrainClass(words)
            self.windTrain.exec()

    def isChecked(self):
        words = {}
        for i in self.radioList:
            if i.isChecked():
                custom_widget = i.parentWidget()
                labels = custom_widget.findChildren(QLabel)
                word = labels[0].text()
                transl = labels[1].text()
                words[word] = transl
        return words

    def swap(self,data):
        swap = {}
        for k,v in data.items():
            swap[v] = k
        return swap

    def  cleanValue(self,data):
        for k,v in data.items():
            data[k] = ''
        return data

if __name__ == '__main__':
    app = QApplication([])
    w = TrainingSettingClass()
    w.show()
    app.exec()
        