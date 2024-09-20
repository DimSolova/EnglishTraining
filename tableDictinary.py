from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widgets import DialogTableDict_ui as ui
import setting

class TableDialogDict(QDialog, ui.Ui_TableDialogDict):
    def __init__(self):
        super(TableDialogDict,self).__init__()
        self.setupUi(self)
        self.stt = setting.setting()
        self.dict = self.stt.get_dictanory()
        #ui
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setColumnCount(2)

        #connect
        self.add_btn.clicked.connect(self.addRow)
        self.del_btn.clicked.connect(self.SelectedItems)

        #start
        self.fillTable()

    def fillTable(self):
        for k, v in self.dict.items():
            self.table.insertRow(self.table.rowCount())
            item = QTableWidgetItem()
            item.setText(k)
            self.table.setItem(self.table.rowCount() - 1, 0, item)

            item = QTableWidgetItem()
            item.setText(v)
            self.table.setItem(self.table.rowCount() - 1, 1, item)

    def addRow(self):
        self.table.insertRow(self.table.rowCount())

    def saveTable(self):
        data = dict()
        for i in range(self.table.rowCount()):
            word = self.table.item(i, 0).text()
            trsl = self.table.item(i, 1).text()
            data[word] = trsl
        return data

    def SelectedItems(self):
        sel_ind = self.table.selectionModel().selectedRows()
        if sel_ind:
            for i in sorted(sel_ind, reverse=True):
                ind = i.row()
                self.deleteRow(ind)

        if self.table.selectedItems():
            for i in self.table.selectedItems():
                ind = i.row()
                self.deleteRow(ind)
        self.saveTable()


    def deleteRow(self,ind):
        word = self.table.item(ind, 0).text()
        del self.dict[word]
        self.table.removeRow(ind)
