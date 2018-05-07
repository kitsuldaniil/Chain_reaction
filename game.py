from enum import Enum
import copy


class FigureState(Enum):
    Init = 0
    Checked = 1
    Current = 2  #текущая позиция фигуры (lastchecked)


class Figure:
    def __init__(self, typ: str, color: str, state: FigureState=FigureState.Init):
        self._typ = typ
        self._color = color
        self._state = state
        self.row = None
        self.column = None
        #self.win = False
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

    @state.setter
    def state(self, value):
        self._state = value


class Game:
    # lastchecked = None
    _figures = []

    def __init__(self, level):
        # level - это путь к файлу в директории levels
        self._tmplist = []
        self._make_level(level)
        self.define_place()
        self.win = False

        if self._figures is not None:
            #self.lastchecked = self._figures[0][0]
            self._figures[0][0].state = FigureState.Current
            self.count_checked = 1 # количество пройденных фигур
            self.list_checked = [self._figures[0][0]]
        ''' painting '''

    @property
    def rows(self):
        return len(self._figures)

    @property
    def columns(self):
        return len(self._figures[0])

    @property
    def get__figures(self):
        return self._figures

    @property
    def figures(self):
        return self._figures

    @figures.setter
    def figures(self, value):
        self._figures = value

    @figures.deleter
    def figures(self):
        self._figures = []

    def _make_level(self, level):  # парсить файл и формировать список списков из фигур по нажатию кнопки Run
        f = open(level, 'r')
        #tmplist = []
        for fig in f:
            self._tmplist.append(Figure(fig.split()[0], fig.split()[1], FigureState.Init))
        f.close()
        self._figures = [self._tmplist[i:i+3] for i in range(0, 9, 3)] #  матрица из фигур 3 на 3


    def define_place(self):         # проверка, в одном ли подсписке (вертикаль/горизонталь)
        for ind, sublist in enumerate(self._figures):
            for j in range(len(sublist)):
                self._figures[ind][j].row = ind
                self._figures[ind][j].column = j

    # def is_may_checked(self, chosen: Figure):          # проверка можно ли пойти в этот элемент (следующий)
    #     if chosen.state == FigureState.Init:
    #         if self.one_place(self.lastchecked, chosen):     #   проверка, находится ли элемент по вертикали или горизонтали
    #             if chosen.color == self.lastchecked.color or chosen.typ == self.lastchecked.typ:
    #                 return True
    #     return False

    def mouse_click(self, chosen: Figure) -> None:
        if len(self.list_checked) == len(self._tmplist):  # win
            self.win = True
            return
        elif chosen.state == FigureState.Init:   # playing
            if self.list_checked[self.count_checked-1].row == chosen.row or \
               self.list_checked[self.count_checked - 1].column == chosen.column:             #  проверка, находится ли элемент по вертикали или горизонтали
                if chosen.color == self.list_checked[self.count_checked - 1].color or \
                   chosen.typ == self.list_checked[self.count_checked - 1].typ:  #  одинаковый тип или фигура
                    self.list_checked[self.count_checked - 1].state = FigureState.Checked    # белый крестик
                    chosen._state = FigureState.Current   #  тёмный крестик
                    self.list_checked.append(chosen)
                    self.count_checked += 1
            if self.count_checked == len(self._tmplist):
                self.win = True
        else:    # if no way out (lose)
            return


"""
читать из файла и создавать вложенные списки из элементов фигур, причём 1-ый элемент выделен крестиком изначально
    далее отдельный метод, проходящийся по матрице и проверяющий может ли быть использован этот элемент(сосед по столбцу или строке)

    мб ещё стоит учесть координаты каждой фигуры, чтобы корректно сделать нажатие мышью??? позишн сопоставляетсяс координатой мыши

    прописать состояние текущей игры !!!
"""