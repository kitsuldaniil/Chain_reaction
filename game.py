class Figure:
    # self.isSelected
    def __init__(self, typ, color):
        self._typ = typ
        self._color = color
        self.checked = False
        self._count = 0
    @property
    def typ(self):
        return self._typ

    @property
    def color(self):
        return self._color

class Game:
    lastchecked = None
    def __init__(self, level):
        self.makelevel(level)
        self.lastchecked = self.figures[0][0] # изначально lastchecked = l[1][1], l[1][1].checked = True
        ''' painting '''

    def _make_level(self, level):  # парсить файл и формировать список списков из фигур по нажатию кнопки Run
        f = open(level, 'r')
        tmplist = []
        for fig in f:
            tmplist.append(Figure(fig.split()[0], fig.split()[1]))
        self.figures = [self.figures[i:i+3] for i in range(0, 9, 3)]
        self.figures[0][0].checked = True

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
        if not chosen.checked:
            if Game.one_place(self.lastchecked, chosen):# проверка, находится ли элемент по вертикали или горизонтали
                if chosen.color == self.lastchecked.color or chosen.typ == self.lastchecked.typ:
                    return True
        return False

    def mouse_click(self, chosen: Figure):
        if self.countchecked == len(self.figures) - 1:  #win
            return
        if self.is_may_checked(chosen):
            chosen.checked = True
            self.lastchecked = chosen
            self.countchecked += 1
        else:    # if no way out
            return

    def draw_figure(self, ):
        pass

    def paint_form(self):




"""
читать из файла и создавать вложенные списки из элементов фигур, причём 1-ый элемент выделен крестиком изначально
    далее отдельный метод, проходящийся по матрице и проверяющий может ли быть использован этот элемент(сосед по столбцу или строке)

    мб ещё стоит учесть координаты каждой фигуры, чтобы корректно сделать нажатие мышью??? позишн сопоставляетсяс координатой мыши
    
    прописать состояние текущей игры !!!
"""



