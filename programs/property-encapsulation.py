class Quadrilateral:

    next_figure_no = 1
    figure_prefix = "Q"

    @classmethod
    def create_without_dimension(cls, **kwargs):
        return cls([], **kwargs)

    @staticmethod
    def _get_figure_no():
        temp = Quadrilateral.next_figure_no
        Quadrilateral.next_figure_no += 1
        return Quadrilateral.figure_prefix + str(temp)

    def __init__(self, dimension, **kwargs):
        self.dimension = dimension
        self.figure_no = self._get_figure_no()


class Square(Quadrilateral):

    next_figure_no = 1
    figure_prefix = "S"
    MAX_SIDES = 4

    # behaves like getter - used to get the value
    @property
    def no_of_sides(self):
        return self._no_of_sides

    # behaves like setter, decorator name must be same as the name of getter
    @no_of_sides.setter
    def no_of_sides(self, sides):
        if sides > Square.MAX_SIDES:
            raise ValueError("Square can't have more then 4 sides.")
        self._no_of_sides = sides

    @staticmethod
    def _get_figure_no():
        temp = Square.next_figure_no
        Square.next_figure_no += 1
        return Square.figure_prefix + str(temp)

    def __init__(self, dimension, *, no_of_sides, **kwargs):
        super().__init__(dimension, **kwargs)
        # if no_of_sides > Square.MAX_SIDES:
        #     raise ValueError("Square can't have more then 4 sides.")
        self.no_of_sides = no_of_sides
        # self encapsulation shown above, validation logic from setter will be executed



q = Quadrilateral.create_without_dimension()
print(q.figure_no)

s = Square.create_without_dimension(no_of_sides=4)
print(s.figure_no, "has", s.no_of_sides, "sides")

# Problem - we are able to skip the check on no_of_sides, this is wrong
s.no_of_sides = 4
print(s.figure_no, "has", s.no_of_sides, "sides")

s.no_of_sides = 8
print(s.figure_no, "has", s.no_of_sides, "sides")