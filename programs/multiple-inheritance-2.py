class Base1:
    def __init__(self):
        print("Base 1 __init__")

class Base2:
    def __init__(self):
        print("Base 2 __init__")

class Base(Base1, Base2):
    pass

b = Base()
