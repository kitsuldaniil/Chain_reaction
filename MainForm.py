import sys
import os
import copy
from MainWin import Ui_MainWin as MainWin
from HelpWin import Ui_HelpWin as HelpWin
from OptionsWin import Ui_OptionsWin as OptionsWin


from game import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QItemDelegate, QApplication, QAction, QTableView, QTableWidget, \
    QTableWidgetItem, QStyleOptionViewItem, QColorDialog
from PyQt5.QtGui import QStandardItemModel, QPainter, QMouseEvent, QIcon, QImage, QFont, QColor, QPalette, QBrush
from PyQt5.QtCore import QModelIndex, QRectF, Qt, QRect


class MainForm(QMainWindow, MainWin):
    def __init__(self, parent=None):    # наверное это наследование
        super().__init__(parent)
        self.setupUi(self)

        self.help_win = None
        self.options_win = None

        self.wid = None
        self.h = None

        # СЛОВАРЬ ИЗОБРАЖЕНИЙ
        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        self._images = {
            os.path.splitext(f)[0]: QImage(os.path.join(images_dir, f))
            for f in os.listdir(images_dir)
        }

        self._game = Game(self.set_level())
        # self.matrix = copy.deepcopy(self._game.figures)    #  ?можно и убрать?
        # self.on_new_game()
        self.make_matrix(self._game)

        class Delegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, m: QModelIndex):
                painter.save()
                self.parent().item_paint(m, painter, option)
                painter.restore()

        # нормальные размеры ячеек
        for i in range(self._game.rows):
            self.tableView.setRowHeight(i, self.cell_size)
        for j in range(self._game.columns):
            self.tableView.setColumnWidth(j, self.cell_size)

        # событие по клику мыши на тэйбл
        def table_mouse_event(e: QMouseEvent) -> None:
            idx = self.tableView.indexAt(e.pos())
            self.mouse_table_clicked(idx, e)

        self.help.triggered.connect(self.show_help)
        self.new_game.triggered.connect(self.on_new_game)
        self.settings.triggered.connect(self.show_options)
        self.tableView.mousePressEvent = table_mouse_event
        self.tableView.setItemDelegate(Delegate(self))
        self.levelspinBox.valueChanged.connect(self.on_new_game)

        self.rect = QRect(self.tableView.x(), self.tableView.y() + self.tableView.height() + 5, self.tableView.width(), 60)
    @property
    def cell_size(self):
        return self.tableView.height()/self._game.columns

    def change_cell_size(self):
        for i in range(self._game.rows):
            self.tableView.setRowHeight(i, self.cell_size)
        for j in range(self._game.columns):
            self.tableView.setColumnWidth(j, self.cell_size)

    # ФОРМИРОВАНИЕ УРОВНЯ В ЗАВИСИМОСТИ ОТ СПИНА
    def set_level(self) -> str:
        return 'levels/level_0' + str(self.levelspinBox.value()) + '.txt'

    # НАЖАТИЕ "НОВАЯ ИГРА" - РАБОТАЕТ!!!
    def on_new_game(self) -> None:
        self._game = Game(self.set_level())
        #  self.matrix = copy.deepcopy(game._figures)
        self.make_matrix(self._game)

    def make_matrix(self, game: Game):
        model = QStandardItemModel(game.rows, game.columns)
        self.tableView.setModel(model)
        self.invalidate()
        self.update()

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

    # ПОздравление с победой
    def paintEvent(self, e):
        if self._game.win:
            qp = QPainter()
            qp.begin(self)
            self.draw_win(qp, e)
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

    def draw_win(self, qp: QPainter, e):
        #  qp = QPainter()
        qp.setPen(QColor(Qt.black))
        qp.setFont(QFont('Comics Sans', 21))
        #r = QRect()
        qp.drawText(self.rect, Qt.AlignBottom, 'CONGRATULATIONS!')

    # open rules
    def show_help(self):
        self.help_win = HelpWindow()
        self.help_win.show()

    # OPEN SETTINGS
    def show_options(self):
        self.options_win = OptionsWindow()

        def set_size():
            self.wid = self.options_win.slider_w.value()
            self.h = self.options_win.slider_h.value()
            self.size(self.wid, self.h)
            self.options_win.label_w.setText(str(self.wid))
            self.options_win.label_h.setText(str(self.h))

        self.options_win.slider_h.valueChanged.connect(set_size)
        self.options_win.slider_w.valueChanged.connect(set_size)

        def change_color():
            col = QColorDialog().getColor()

            if col.isValid():
                self.set_color(col)

        self.options_win.btn_color.clicked.connect(change_color)
        self.options_win.show()

    def set_color(self, color: QColor):
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(color))
        self.setPalette(palette)

    def size(self, width: int, height: int):
        prev_w = self.width()
        prev_h = self.height()

        self.levelspinBox.move(self.levelspinBox.x()+(width - prev_w), self.levelspinBox.y())
        self.label.move(self.label.x()+(width - prev_w), self.label.y())
        self.setFixedSize(width, height)
        self.tableView.setFixedSize(self.tableView.width() + (width - prev_w),
                                    self.tableView.height() + (height - prev_h))
        #self.rect.moveTo(self.rect.x(), self.rect.y() + (height - prev_h))
        self.rect.setRect(self.rect.x(), self.rect.y(),
                          self.rect.width()+(width - prev_w), self.rect.height()+(height - prev_h))
        self.change_cell_size()


class OptionsWindow(QMainWindow, OptionsWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class HelpWindow(QMainWindow, HelpWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
