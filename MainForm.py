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
        self.gam = None
        lvl = 'levels/level_0' + str(self.levelspinBox.value()) + '.txt'

        images_dir = os.path.join(os.path.dirname(__file__), 'images')  # СЛОВАРЬ ИЗОБРАЖЕНИЙ
        self._images = {
            os.path.splitext(f)[0]: QImage(os.path.join(images_dir, f))
            for f in os.listdir(images_dir)
        }

        self._game = Game(lvl)
        self.matrix = copy.deepcopy(self._game.get_figures)   # ?можно и убрать?
        self.make_matrix(self._game)    # мб убрать

        self.settings.triggered.connect(self.show_help)
        self.new_game.triggered.connect(self.on_new_game)

        class Delegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, m: QModelIndex):
                painter.save()
                self.parent().item_paint(m, painter, option)
                painter.restore()
        #self.tableView.rowHeight(83)
        #self.tableView.setColumnWidth(2, 83)

        for i in range(self._game.rows):
            self.tableView.setRowHeight(i, 85)
        for j in range(self._game.columns):
            self.tableView.setColumnWidth(j, 85)

        self.tableView.mousePressEvent = self.table_mouse
        self.tableView.setItemDelegate(Delegate(self))


    def set_level(self):   # ФОРМИРОВАНИЕ УРОВНЯ В ЗАВИСИМОСТИ ОТ СПИНА
          return 'levels/level_0' + str(self.levelspinBox.value()) + '.txt'

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
        self._game == Game(self.set_level())
        self.matrix = None
        self.matrix = copy.deepcopy(self._game.figures)
        self.make_matrix(self._game)

    def item_paint(self, m: QModelIndex, painter: QPainter, options: QStyleOptionViewItem):
        item = self._game.figures[m.row()][m.column()]
        color_type = str(item.color) + '_' + str(item.typ)
        if item.state == FigureState.Init:
            img = self._images[color_type+'_init']
        elif item.state == FigureState.Checked:
            img = self._images[color_type + '_checked']
        else:
            img = self._images[color_type + '_current']


        painter.drawImage(QRectF(options.rect), img)
        #self.update()


    def table_mouse(self, e: QMouseEvent):
        idx = self.tableView.indexAt(e.pos())
        self.mouse_table_clicked(idx, e)

    def mouse_table_clicked(self, m: QModelIndex, e: QMouseEvent=None):
        if e.button() == Qt.LeftButton:
            self._game.mouse_click(self.matrix[m.row()][m.column()])
        else:
            return
        self.invalidate()
        self.update()

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
