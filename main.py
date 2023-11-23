import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class MainUiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(779, 475)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.table, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtWidgets.QPushButton(Form)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.create = QtWidgets.QPushButton(Form)
        self.create.setObjectName("create")
        self.horizontalLayout.addWidget(self.create)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.tip = QtWidgets.QLabel(Form)
        self.tip.setObjectName("tip")
        self.gridLayout.addWidget(self.tip, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "идентификатор"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "название сорта"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "степень обжарки"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "молотый/в зернах"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "описание вкуса"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "цена руб."))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("Form", "объем упаковки л."))
        self.update.setText(_translate("Form", "Изменить"))
        self.label.setText(_translate("Form", "Кофе"))
        self.create.setText(_translate("Form", "Добавить"))
        self.tip.setText(_translate("Form", "Нажмите на строку, данные которой хотите изменить"))


class SecondUiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(899, 657)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.id = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.horizontalLayout.addWidget(self.id)
        self.create = QtWidgets.QPushButton(Form)
        self.create.setObjectName("create")
        self.horizontalLayout.addWidget(self.create)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.class_2 = QtWidgets.QLineEdit(Form)
        self.class_2.setObjectName("class_2")
        self.horizontalLayout_2.addWidget(self.class_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.degree = QtWidgets.QLineEdit(Form)
        self.degree.setObjectName("degree")
        self.horizontalLayout_2.addWidget(self.degree)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.price = QtWidgets.QDoubleSpinBox(Form)
        self.price.setMaximum(100000.0)
        self.price.setObjectName("price")
        self.horizontalLayout_4.addWidget(self.price)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.volume = QtWidgets.QDoubleSpinBox(Form)
        self.volume.setMaximum(100000.0)
        self.volume.setObjectName("volume")
        self.horizontalLayout_4.addWidget(self.volume)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.type = QtWidgets.QLineEdit(Form)
        self.type.setObjectName("type")
        self.horizontalLayout_3.addWidget(self.type)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.taste = QtWidgets.QLineEdit(Form)
        self.taste.setObjectName("taste")
        self.horizontalLayout_3.addWidget(self.taste)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Данные кофе"))
        self.label_8.setText(_translate("Form", "№"))
        self.id.setText(_translate("Form", "1"))
        self.create.setText(_translate("Form", "Готово"))
        self.label_2.setText(_translate("Form", "сорт"))
        self.label_3.setText(_translate("Form", "степень прожарки"))
        self.label_6.setText(_translate("Form", "цена"))
        self.label_7.setText(_translate("Form", "объем упаковки"))
        self.label_4.setText(_translate("Form", "молотый/растворимый"))
        self.label_5.setText(_translate("Form", "описание вкуса"))
        self.label_9.setText(_translate("Form", "Данные таблицы обновятся после того, как вы нажмете "
                                                "*готово* и закроете это окно"))


class Information(QWidget, MainUiForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = sqlite3.connect("data/coffee.sqlite")
        self.query = self.database.cursor()
        self.refill_table()
        self.window = None
        self.create.clicked.connect(self.click)
        self.update.clicked.connect(self.click)
        self.tip.hide()
        self.show()

    def refill_table(self):
        self.table.setRowCount(0)
        for i, elem in (enumerate(self.query.execute("SELECT * FROM coffee"))):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(str(elem[j])))

    def click(self):
        self.tip.hide()
        if self.sender().text() == "Изменить":
            data = list()
            for i in range(self.table.columnCount()):
                try:
                    data.append(self.table.item(self.table.selectedItems()[0].row(), i))
                except IndexError:
                    self.tip.show()
                    return
            self.window = ChangeScreen(self, self.database, self.query, data)
        else:
            self.window = ChangeScreen(self, self.database, self.query)


class ChangeScreen(QWidget, SecondUiForm):
    def __init__(self, parent, database, query, items=None):
        super().__init__()
        self.setupUi(self)
        self.query = query
        self.database = database
        self.parent = parent
        if not items:
            self.id.hide()
            self.label_8.hide()
            self.create.clicked.connect(lambda: self.query.execute("INSERT INTO "
                                                                   "coffee(class, degree_of_roasting, type, taste, "
                                                                   "price, volume) "
                                                                   f"VALUES('{self.class_2.text()}', "
                                                                   f"'{self.degree.text()}', '{self.type.text()}', "
                                                                   f"'{self.taste.text()}', {self.price.value()}, "
                                                                   f"{self.volume.value()})"))
        else:
            for field, value in zip((self.class_2, self.degree, self.type, self.taste, self.price, self.volume),
                                    items[1:]):
                try:
                    field.setText(value.text())
                except AttributeError:
                    field.setValue(float(value.text()))
            self.create.clicked.connect(lambda: self.query.execute("UPDATE coffee "
                                                                   f"SET class = '{self.class_2.text()}', "
                                                                   f"degree_of_roasting = '{self.degree.text()}', "
                                                                   f"type = '{self.type.text()}', "
                                                                   f"taste = '{self.taste.text()}', "
                                                                   f"price = {self.price.value()}, "
                                                                   f"volume =  {self.volume.value()} "
                                                                   f"WHERE id = {items[0].text()}"))

        self.show()

    def closeEvent(self, event):
        self.database.commit()
        self.parent.refill_table()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Information()
    sys.exit(app.exec())
