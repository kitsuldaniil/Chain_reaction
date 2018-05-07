import sys
import os
import copy
from MainWin import Ui_MainWin as MainWin
from HelpWin import Ui_HelpWin as HelpWin


from game import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QItemDelegate, QApplication, QAction, QTableView, QTableWidget, \
    QTableWidgetItem, QStyleOptionViewItem, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QPainter, QMouseEvent, QIcon, QImage, QFont, QColor
from PyQt5.QtCore import QModelIndex, QRectF, Qt, QRect


class MainForm(QMainWindow, MainWin):
    def __init__(self, parent=None):    # наверное это наследование
        super().__init__(parent)
        self.setupUi(self)

        self.help = None

        lvl = 'levels/level_0' + str(self.levelspinBox.value()) + '.txt'

        # СЛОВАРЬ ИЗОБРАЖЕНИЙ
        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        self._images = {
            os.path.splitext(f)[0]: QImage(os.path.join(images_dir, f))
            for f in os.listdir(images_dir)
        }

        self._game = Game(self.set_level())
        #self.matrix = copy.deepcopy(self._game._figures)    #  ?можно и убрать?
        #self.on_new_game()
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

        # нормальные размеры ячеек
        for i in range(self._game.rows):
            self.tableView.setRowHeight(i, 85)
        for j in range(self._game.columns):
            self.tableView.setColumnWidth(j, 85)

        # событие по клику мыши на тэйбл
        def table_mouse_event(e: QMouseEvent) -> None:
            idx = self.tableView.indexAt(e.pos())
            self.mouse_table_clicked(idx, e)

        self.tableView.mousePressEvent = table_mouse_event
        self.tableView.setItemDelegate(Delegate(self))

    # ФОРМИРОВАНИЕ УРОВНЯ В ЗАВИСИМОСТИ ОТ СПИНА
    def set_level(self) -> str:
        return 'levels/level_0' + str(self.levelspinBox.value()) + '.txt'

    # def on_new_game(self) -> None:  # НАЖАТИЕ "НОВАЯ ИГРА"
    #    #self._game = None
    #     self._game == Game(self.set_level())
    #     # self.matrix = None
    #     self.matrix = copy.deepcopy(self._game._figures)
    #     self.make_matrix(self._game)

    # НАЖАТИЕ "НОВАЯ ИГРА" - нифига не работает
    def on_new_game(self) -> None:
        self._game == Game(self.set_level())
        #  self.matrix = None
        #  self.matrix = copy.deepcopy(game._figures)
        self.make_matrix(self._game)

    def show_help(self):           # open rules
        self.help = HelpWindow()
        self.help.show()

    def make_matrix(self, game: Game):
        model = QStandardItemModel(game.rows, game.columns)
        self.tableView.setModel(model)
        self.invalidate()
        self.update()

    '''
              widget = QTableWidget(game.rows, game.columns)
              self.matrix = copy.deepcopy(self.game._figures)
                  for i in range(game.rows):
                 for j in range(game.columns):
                     item = QTableWidgetItem(self.matrix[i][j])
                     widget.setItem(game.rows, game.columns, item)
                     widget.setIcon
                     '''
    # отрисовка фигур
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

        #   if self._game.win:
        #   self.draw_win(painter, options)
        #   self.update()

    # ПОздравление с победой
    def paintEvent(self, e):
        if self._game.win:
            qp = QPainter()
            qp.begin(self)
            MainForm.draw_win(qp, e)
            qp.end()

    # по клику мыши
    def mouse_table_clicked(self, m: QModelIndex, e: QMouseEvent=None):
        if e.button() == Qt.LeftButton:
            self._game.mouse_click(self._game.figures[m.row()][m.column()])
        else:
            return
        self.invalidate()
        self.update()

    def invalidate(self):
        self.tableView.viewport().update()

    @staticmethod
    def draw_win(qp: QPainter, e):
        #  qp = QPainter()
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Comics Sans', 24))
        qp.drawText(e.rect(), Qt.AlignBottom, 'CONGRATULATIONS!')


'''
при запуске открывается форма с созданной игрой с исходным 1 уровнем
при нажатии на "Новая игра" брать значение спина и в зависимости от него создавать игру с опр уровнем
'''


class HelpWindow(QMainWindow, HelpWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #  self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
