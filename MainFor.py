import sys
import os
import copy
from MainTest import Ui_MainTest as MainTest
from HelpWin import Ui_HelpWin as HelpWin

from game import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QItemDelegate, QApplication, QAction, QTableView, QTableWidget, \
    QTableWidgetItem, QStyleOptionViewItem
from PyQt5.QtGui import QStandardItemModel, QPainter, QMouseEvent, QIcon, QImage, QFont, QColor
from PyQt5.QtCore import QModelIndex, QRectF, Qt
from PyQt5 import QtSvg


class MainFor(QMainWindow, MainTest):
    def __init__(self, parent=None):  # наверное это наследование
        super().__init__(parent)
        self.setupUi(self)
        self.help = None

        self.matrix = [[(i, j) for j in range(3)] for i in range(3)]

        self.tableWidget.mousePressEvent = self.paintEvent
        # QtSvg.QSvgRenderer(os.path.join(images_dir, f))

       # self.tableView.setItemDelegate(Delegate(self))

    #def mousePressEvent(self, e):


        # qp.begin(self)
        # qp.setPen(Qt.red)
        # qp.setFont(QFont('Decorative', 16))
        # qp.drawText(5, 8, 'Congratulations')
        # qp.end()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(0, 0, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(0, 15, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(0, 15, 90, 60)

    def show_help(self):  # open rules
        self.help = HelpWindow()
        self.help.show()


    def drawing(self):
        qt = QPainter()
        qp.setPen(QColor(Qt.Red))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, 'Congratulations')
        #self.tableWidget = QTableWidget(3, 3)
        # icon = QIcon('images/red_round_init.png')
        # for i in range(3):
        #     for j in range(3):
        #         item = QTableWidgetItem(0)
        #         item.setIcon(icon)
        #         self.tableWidget.setItem(i, j, item)
        #         self.tableWidget.setWindowIcon(icon)
        #
        # self.tableWidget.viewport().update()
        # p.restore()



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
