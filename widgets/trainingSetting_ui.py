# Form implementation generated from reading ui file '/Users/dima/PycharmProjects/EnglishLearning/widgets/trainingSetting.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TrainingSetting(object):
    def setupUi(self, TrainingSetting):
        TrainingSetting.setObjectName("TrainingSetting")
        TrainingSetting.resize(527, 334)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TrainingSetting)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWords_lw = QtWidgets.QListWidget(parent=TrainingSetting)
        self.listWords_lw.setObjectName("listWords_lw")
        self.verticalLayout_2.addWidget(self.listWords_lw)
        self.start_btn = QtWidgets.QPushButton(parent=TrainingSetting)
        self.start_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout_2.addWidget(self.start_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectLang_cb = QtWidgets.QComboBox(parent=TrainingSetting)
        self.selectLang_cb.setObjectName("selectLang_cb")
        self.selectLang_cb.addItem("")
        self.selectLang_cb.addItem("")
        self.verticalLayout.addWidget(self.selectLang_cb)
        self.showAnsw_cb = QtWidgets.QCheckBox(parent=TrainingSetting)
        self.showAnsw_cb.setChecked(True)
        self.showAnsw_cb.setObjectName("showAnsw_cb")
        self.verticalLayout.addWidget(self.showAnsw_cb)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(TrainingSetting)
        QtCore.QMetaObject.connectSlotsByName(TrainingSetting)

    def retranslateUi(self, TrainingSetting):
        _translate = QtCore.QCoreApplication.translate
        TrainingSetting.setWindowTitle(_translate("TrainingSetting", "Dialog"))
        self.start_btn.setText(_translate("TrainingSetting", "startTraining"))
        self.selectLang_cb.setItemText(0, _translate("TrainingSetting", "English - Russian"))
        self.selectLang_cb.setItemText(1, _translate("TrainingSetting", "Russian - English"))
        self.showAnsw_cb.setText(_translate("TrainingSetting", "show Answer"))
