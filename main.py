import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem


class Information(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.query = sqlite3.connect("coffee.sqlite").cursor()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.table.setRowCount(0)
        for i, elem in (enumerate(self.query.execute("SELECT * FROM coffee"))):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(str(elem[1:][j])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Information()
    sys.exit(app.exec())
