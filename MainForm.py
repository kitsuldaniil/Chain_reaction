import sys
import os
import copy
from MainWin import Ui_MainWin as MainWin
from HelpWin import Ui_HelpWin as HelpWin


from game import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QItemDelegate, QApplication, QAction, QTableView, QTableWidget, \
    QTableWidgetItem, QStyleOptionViewItem, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QPainter, QMouseEvent, QIcon, QImage
from PyQt5.QtCore import QModelIndex, QRectF, Qt, QRect


class MainForm(QMainWindow, MainWin):
    def __init__(self, parent=None):    # наверное это наследование
        super().__init__(parent)
        self.setupUi(self)

        self.help = None
        lvl = 'levels/level_0' + str(self.levelspinBox.value()) + '.txt'


        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        self._images = {
            os.path.splitext(f)[0]: QImage(os.path.join(images_dir, f))
            for f in os.listdir(images_dir)
        }
       # QtSvg.QSvgRenderer(os.path.join(images_dir, f))
        self.game = Game(lvl)
        self.matrix = copy.deepcopy(self.game.figures)
        self.make_matrix(self.game)    # мб убрать

        self.settings.triggered.connect(self.show_help)  # работает
        self.new_game.triggered.connect(self.on_new_game)

        class Delegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, m: QModelIndex):
                painter.save()

                self.parent().item_paint(m, painter, option)
                painter.restore()
       # self.tableView.rowHeight(83)
        #self.tableView.setColumnWidth(2, 83)
        for i in range(self.game.rows):
            self.tableView.setRowHeight(i, 85)
        for j in range(self.game.columns):
            self.tableView.setColumnWidth(j, 85)
        self.tableView.mousePressEvent = self.mouse_table_clicked
        self.tableView.setItemDelegate(Delegate(self))


    def _level(self):   # ФОРМИРОВАНИЕ УРОВНЯ В ЗАВИСИМОСТИ ОТ СПИНА
        if self.levelspinBox.value == 2:
            return 'levels/level_02.txt'
        return 'levels/level_01.txt'

    def show_help(self):           # open rules
        self.help = HelpWindow()
        self.help.show()

    def make_matrix(self, game: Game):
        model = QStandardItemModel(game.rows, game.columns)
        self.tableView.setModel(model)
        self.invalidate()
        self.update()

         # widget = QTableWidget(game.rows, game.columns)
         # self.matrix = copy.deepcopy(self.game.figures)
         # for i in range(game.rows):
         #     for j in range(game.columns):
         #         item = QTableWidgetItem(self.matrix[i][j])
         #         widget.setItem(game.rows, game.columns, item)
         #         widget.setIco

    def on_new_game(self):     # НАЖАТИЕ "НОВАЯ ИГРА"
        lvl = self._level()
        self.game == Game(lvl)
        self.make_matrix(self.game)

    def item_paint(self, m: QModelIndex, painter: QPainter, options: QStyleOptionViewItem):
        item = self.matrix[m.row()][m.column()]
        color_type = str(item.color) + '_' + str(item.typ)
        if item.state == FigureState.Init:
            img = self._images[color_type+'_init']
        if item.state == FigureState.Checked:
            img = self._images[color_type + '_checked']
        else:
            img = self._images[color_type + '_current']

        #rect = QRect(m.x(), m.y(), 83, 83)
        painter.drawImage(QRectF(options.rect), img)
        self.update()  # shit

        #img.render(painter, QRectF(options.rect))



    def mouse_table_clicked(self, m: QModelIndex, e: QMouseEvent=None, painter: QPainter=None, options: QStyleOptionViewItem=None):
        if e.button() == Qt.LeftButton:
            self.game.mouse_click(self.matrix[m.row()][m.column()])
        else:
            return
        self.invalidate()

    def invalidate(self):
        self.tableView.viewport().update()





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
    win = MainForm()
    win.show()
    sys.exit(app.exec_())