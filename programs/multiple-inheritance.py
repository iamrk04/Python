class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"{type(self).__name__}({self._items})"


class SortedList(SimpleList):
    def __init__(self, items=()):
        print(super())          # pay attention here as well
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        s = super()
        print(s)
        super().__init__(items) # instance bound super proxy
        print(s.__init__)       # MRO from self, find class after this class in MRO
    
    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList only supports integer values.")
    
    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass


sl = SimpleList([5, 1, 3, 4, 2])
print(len(sl))
print(sl)
print()

sil = SortedIntList([5, 1, 3, 4, 2])
print(sil)
print()

# sil = SortedIntList([5, 1, 3, 4.1, 2])
# print(sil)
# sil.add(4.8)
# print(sil)

print(SortedIntList.__mro__)