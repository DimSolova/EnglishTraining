# Form implementation generated from reading ui file '/Users/dima/PycharmProjects/EnglishLearning/widgets/trainingSatting.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TrainingSetting(object):
    def setupUi(self, TrainingSetting):
        TrainingSetting.setObjectName("TrainingSetting")
        TrainingSetting.resize(400, 300)
        self.listWords_lw = QtWidgets.QListWidget(parent=TrainingSetting)
        self.listWords_lw.setGeometry(QtCore.QRect(20, 10, 256, 192))
        self.listWords_lw.setObjectName("listWords_lw")
        self.start_btn = QtWidgets.QPushButton(parent=TrainingSetting)
        self.start_btn.setGeometry(QtCore.QRect(20, 220, 113, 32))
        self.start_btn.setObjectName("start_btn")

        self.retranslateUi(TrainingSetting)
        QtCore.QMetaObject.connectSlotsByName(TrainingSetting)

    def retranslateUi(self, TrainingSetting):
        _translate = QtCore.QCoreApplication.translate
        TrainingSetting.setWindowTitle(_translate("TrainingSetting", "Dialog"))
        self.start_btn.setText(_translate("TrainingSetting", "startTraining"))
