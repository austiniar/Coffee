import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QDoubleSpinBox, QLineEdit


class Information(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.database = sqlite3.connect("coffee.sqlite")
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


class ChangeScreen(QWidget):
    def __init__(self, parent, database, query, items=None):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
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
