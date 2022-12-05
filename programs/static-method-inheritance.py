class Quadrilateral:

    next_figure_no = 1
    figure_prefix = "Q"

    @staticmethod
    def _get_figure_no():
        temp = Quadrilateral.next_figure_no
        Quadrilateral.next_figure_no += 1
        return Quadrilateral.figure_prefix + str(temp)

    def __init__(self, dimension):
        self.dimension = dimension
        self.figure_no = self._get_figure_no()
                        # the self keyword is very important here
                        # for static method inheritance to work


class Square(Quadrilateral):

    next_figure_no = 1
    figure_prefix = "S"

    @staticmethod
    def _get_figure_no():
        temp = Square.next_figure_no
        Square.next_figure_no += 1
        return Square.figure_prefix + str(temp)


q = Quadrilateral([10, 12, 14, 16])
print(q.figure_no)

q = Quadrilateral([11, 13, 15, 17])
print(q.figure_no)

s = Square([10, 10, 10, 10])
print(s.figure_no)