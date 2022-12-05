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
print(dir(v))
print(v.__dict__)
print(type(v.__dict__))
v.__dict__['x'] = 100
print(v.x)

print()

print(hasattr(v, 'z'))
print(getattr(v, 'x'))
setattr(v, 'z', 0)
delattr(v, 'z')