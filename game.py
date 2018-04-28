class Figure:
    # self.isSelected
    def __init__(self, type, color):
        self.type = type
        self.color = color
        self.isSelected = False
        self.can_used = False


class Game:
    def __init__(self):
        self.figures = []

    self.lastchecked
    ''' поле для последнего выбранного'''
    self.thenckecked  # мб и не надо

    def makelevel(self, path):  # парсить файл и формировать список списков из фигур
        f = open(path, 'r')
        for fig in f:
            self.figures.append(Figure(fig.split()[0], fig.split()[1]))
        tmplist = self.figures.copy()
        while i <= len(tmplist):
            prev = i
            i += 3
            self.figures[] = [[self.figures[prev:i]] for s in range(3)]

        '''
        изначально
        lastckecked = l[1][1], l[1][1].checked = True
        '''

    def is_may_checked(self, lastchecked, thenchecked):  # проверка можно ли пойти в этот элемент (следующий)
        return True


"""читать из файла и создавать вложенные списки из элементов фигур, причём 1-ый элемент выделен крестиком изначально
    далее отдельный метод, проходящийся по матрице и проверяющий может ли быть использован этот элемент(сосед по столбцу или строке)

    мб ещё стоит учесть координаты каждой фигуры, чтобы корректно сделать нажатие мышью??? позишн сопоставляетсяс координатой мыши

"""



