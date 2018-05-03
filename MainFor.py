import sys
import os
import copy
from MainTest import Ui_MainTest as MainTest
from HelpWin import Ui_HelpWin as HelpWin

from game import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QItemDelegate, QApplication, QAction, QTableView, QTableWidget, \
    QTableWidgetItem, QStyleOptionViewItem
from PyQt5.QtGui import QStandardItemModel, QPainter, QMouseEvent, QIcon, QImage
from PyQt5.QtCore import QModelIndex, QRectF, Qt
from PyQt5 import QtSvg


class MainFor(QMainWindow, MainTest):
    def __init__(self, parent=None):  # наверное это наследование
        super().__init__(parent)
        self.setupUi(self)
        self.help = None

        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        self._images = {
            os.path.splitext(f)[0]: QImage(os.path.join(images_dir, f))
            # словарь с иконками
            for f in os.listdir(images_dir)
        }
        self.matrix = [[(i, j) for j in range(3)]for i in range(3)]
        self.drawing()
        # QtSvg.QSvgRenderer(os.path.join(images_dir, f))

       # self.tableView.setItemDelegate(Delegate(self))

    #def mousePressEvent(self, e):

    def paintEvent(self, e):
        p = QPainter(self)

    def show_help(self):  # open rules
        self.help = HelpWindow()
        self.help.show()


    def drawing(self):
        p = QPainter(self)
        p.save()
        #self.tableWidget = QTableWidget(3, 3)
        icon = QIcon('images/red_round_init.png')
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(0)
                item.setIcon(icon)
                self.tableWidget.setItem(i, j, item)
                self.tableWidget.setWindowIcon(icon)

        self.tableWidget.viewport().update()
        p.restore()



        # img.render(painter, QRectF(options.rect))

'''

при запуске открывается форма с созданной игрой с исходным 1 уровнем
при нажатии на "Новая игра" брать значение спина и в зависимости от него создавать игру с опр уровнем

'''


class HelpWindow(QMainWindow, HelpWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainFor()
    win.show()
    sys.exit(app.exec_())
