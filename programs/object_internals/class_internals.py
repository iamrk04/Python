class Vector:
    """
    A 2-dimensional vector.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y})"


v = Vector(2, 3)
print(v.__class__.__dict__)
print(type(v.__class__.__dict__))

setattr(v.__class__, "some_var", 0)
print(v.__class__.__dict__)
print(v.__dict__)