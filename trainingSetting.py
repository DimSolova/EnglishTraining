from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widgets import trainingSatting_ui as ui
import setting

class TrainingSettingClass(QDialog,ui.Ui_TrainingSetting):
    def __init__(self):
        super(TrainingSettingClass,self).__init__()
        self.setupUi(self)
        self.stt = setting.setting()

        #start
        self.fillList()

    def fillList(self):
        data = self.stt.get_dictanory()
        if data:
            for k, v in data.items():
                customWidget = QWidget()
                layout = QHBoxLayout(customWidget)

                radio = QRadioButton()
                layout.addWidget(radio)

                text = QLabel(f"{k}-{v}")
                layout.addWidget(text)

                customWidget.setLayout(layout)  # Set the layout for the custom widget

                listWidgetItem = QListWidgetItem()
                listWidgetItem.setSizeHint(customWidget.sizeHint())  # Set the size hint for proper display

                self.listWords_lw.addItem(listWidgetItem)  # Add the encapsulated custom widget
                self.listWords_lw.setItemWidget(listWidgetItem, customWidget)  # Set the custom widget for the item


if __name__ == '__main__':
    app = QApplication([])
    w = TrainingSettingClass()
    w.show()
    app.exec()
        