from enum import Enum
import copy

class FigureState(Enum):
    Init = 0
    Checked = 1
    Current = 2  #текущая позиция фигуры (lastchecked)


class Figure:
    # self.isSelected
    def __init__(self, typ, color, state: FigureState=FigureState.Init):
        self._typ = typ
        self._color = color
        self._state = state
        self.row = None
        self.column = None
        #self._count = 0

    @property
    def typ(self):
        return self._typ

    @property
    def color(self):
        return self._color

    @property
    def state(self) -> FigureState:
        return self._state

    # @state.setter
    # def state(self, value):
    #     self._state = value

class Game:
    lastchecked = None
    def __init__(self, level):  # level - это путь к файлу в директории levels
        #self.level = level
        self.figures = None
        self._tmplist = []
        self._make_level(level)
        self.define_place()

        if self.figures != None:
            self.lastchecked = self.figures[0][0]
            self.figures[0][0]._state = FigureState.Current
            self.countchecked = 1 # количество пройденных фигур
            self.list_checked = [self.figures[0][0]]
        ''' painting '''

    @property
    def rows(self):
        return len(self.figures)

    @property
    def columns(self):
        return len(self.figures[0])

    @property
    def get_figures(self):
        return self.figures

    def _make_level(self, level):  # парсить файл и формировать список списков из фигур по нажатию кнопки Run
        f = open(level, 'r')
        #tmplist = []
        for fig in f:
            self._tmplist.append(Figure(fig.split()[0], fig.split()[1], FigureState.Init))
        self.figures = [self._tmplist[i:i+3] for i in range(0, 9, 3)] #  матрица из фигур 3 на 3


    def define_place(self):         # проверка, в одном ли подсписке (вертикаль/горизонталь)
        # for ind, sublist in enumerate(self.figures):
        #     if fig1 in sublist and fig2 in sublist:
        #         return True

        # for ind, sublist in enumerate(list(zip(*self.figures))):
        #     if fig1 in sublist and fig2 in sublist:
        #         return True

        for ind, sublist in enumerate(self.figures):
            for j in range(len(sublist)):
                self.figures[ind][j].row = ind
                self.figures[ind][j].column = j
        # for ind, sublist in enumerate(list(zip(*self.figures))):
        #     for j in range(len(sublist)):
        #         self.figures[ind][j].column = ind

        # return False



    def is_may_checked(self, chosen: Figure):          # проверка можно ли пойти в этот элемент (следующий)
        if chosen.state == FigureState.Init:
            if self.one_place(self.lastchecked, chosen):     # проверка, находится ли элемент по вертикали или горизонтали
                if chosen.color == self.lastchecked.color or chosen.typ == self.lastchecked.typ:
                    return True
        return False

    def mouse_click(self, chosen: Figure) -> None:
        if len(self.list_checked) == len(self._tmplist):  # win
            return
        elif chosen.state == FigureState.Init:   # playing
            if self.list_checked[self.countchecked-1].row == chosen.row or \
                self.list_checked[self.countchecked - 1].column == chosen.column:             #  проверка, находится ли элемент по вертикали или горизонтали
                if chosen.color == self.list_checked[self.countchecked - 1].color or \
                        chosen.typ == self.list_checked[self.countchecked - 1].typ:  #  одинаковый тип или фигура
                    self.list_checked[self.countchecked - 1]._state = FigureState.Checked    # белый крестик
                    chosen._state = FigureState.Current   #       тёмный крестик
                    #self.lastchecked = chosen
                    self.list_checked.append(chosen)
                    self.countchecked += 1
        else:    # if no way out (lose)
            return


   # def paint_form(self):

"""
читать из файла и создавать вложенные списки из элементов фигур, причём 1-ый элемент выделен крестиком изначально
    далее отдельный метод, проходящийся по матрице и проверяющий может ли быть использован этот элемент(сосед по столбцу или строке)

    мб ещё стоит учесть координаты каждой фигуры, чтобы корректно сделать нажатие мышью??? позишн сопоставляетсяс координатой мыши

    прописать состояние текущей игры !!!
"""