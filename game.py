from enum import Enum

class FigureState(Enum):
    Init = 0
    Checked = 1
    Current = 2


class Figure:
    # self.isSelected
    def __init__(self, typ, color, state: FigureState = FigureState.Init):
        self._typ = typ
        self._color = color
        self._state = state
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
    lastchecked = None
    def __init__(self, level):
        self.figures = None
        self._make_level(level)
        if self.figures != None:
            self.lastchecked = self.figures[0][0]
            self.figures[0][0].state = FigureState.Current
            # изначально lastchecked = l[1][1], l[1][1].checked = True
        ''' painting '''

    @property
    def rows(self):
        return len(self.figures)

    @property
    def columns(self):
        return len(self.figures[0])

    def _make_level(self, level):  # парсить файл и формировать список списков из фигур по нажатию кнопки Run
        f = open(level, 'r')
        tmplist = []
        for fig in f:
            tmplist.append(Figure(fig.split()[0], fig.split()[1], FigureState.Init))
        self.figures = [tmplist[i:i+3] for i in range(0, 9, 3)]


        '''
        изначально
        lastckecked = l[1][1], l[1][1].checked = True
        '''
    @staticmethod
    def one_place(self, el, el2): # проверка, в одном ли подсписке
        for ind, sublist in enumerate(self.figures):
            if el1 in sublist and el2 in sublist:
                return True

        for ind, sublist in enumerate(list(zip(*self.figures))):
            if el1 in sublist and el2 in sublist:
                return True
        return False



    def is_may_checked(self, chosen: Figure):  # проверка можно ли пойти в этот элемент (следующий)
        if not chosen.state == FigureState.Init:
            if Game.one_place(self.lastchecked, chosen):# проверка, находится ли элемент по вертикали или горизонтали
                if chosen.color == self.lastchecked.color or chosen.typ == self.lastchecked.typ:
                    return True
        return False

    def mouse_click(self, chosen: Figure):
        if self.countchecked == len(self.figures) - 1:  # win
            return
        if self.is_may_checked(chosen):
            self.lastchecked.state = FigureState.Checked  # будет ли работать?
            chosen.state = FigureState.Current
            self.lastchecked = chosen
            self.countchecked += 1
        else:    # if no way out (lose)
            return

    def draw_figure(self, ):
        pass

   # def paint_form(self):

"""
читать из файла и создавать вложенные списки из элементов фигур, причём 1-ый элемент выделен крестиком изначально
    далее отдельный метод, проходящийся по матрице и проверяющий может ли быть использован этот элемент(сосед по столбцу или строке)

    мб ещё стоит учесть координаты каждой фигуры, чтобы корректно сделать нажатие мышью??? позишн сопоставляетсяс координатой мыши

    прописать состояние текущей игры !!!
"""