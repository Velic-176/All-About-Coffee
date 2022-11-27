import sys
import sqlite3
from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Types of coffee')

        self.con = sqlite3.connect('coffee.db')
        self.bd = self.con.cursor()

        self.table.setColumnWidth(0, 20)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 120)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 100)

        self.fill_the_table()

    def fill_the_table(self):
        coffees = self.bd.execute("""SELECT types.ID,
                                  types.name,
                                  types.degree_of_roast,
                                  GroundOrInBeans.condition,
                                  types.taste,
                                  types.price,
                                  types.package_size
                           FROM types
                           INNER JOIN GroundOrInBeans
                           ON GroundOrInBeans.ID = types.ground_or_beans""").fetchall()

        length = len(coffees)
        self.table.setRowCount(length)
        for i in range(length):
            self.table.setItem(i, 0, QTableWidgetItem(str(coffees[i][0])))
            self.table.setItem(i, 1, QTableWidgetItem(str(coffees[i][1])))
            self.table.setItem(i, 2, QTableWidgetItem(str(coffees[i][2])))
            self.table.setItem(i, 3, QTableWidgetItem(str(coffees[i][3])))
            self.table.setItem(i, 4, QTableWidgetItem(str(coffees[i][4])))
            self.table.setItem(i, 5, QTableWidgetItem(str(coffees[i][5])))
            self.table.setItem(i, 6, QTableWidgetItem(str(coffees[i][6])))

            font = QFont()
            font.setPointSize(10)
            [self.table.item(i, j).setFont(font) for j in range(7)]


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

