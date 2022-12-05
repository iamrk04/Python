from InOrderIterator import InOrderIterator


missing = object()


class SkipMissingIterator:

    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item
    
    def __iter__(self):
        return self


#               +
#       r               *
#                   p       q

if __name__ == "__main__":
    expr_tree = ["+", "r", "*", missing, missing, "p", "q"]
    iterator = SkipMissingIterator(expr_tree)
    print(" ".join(iterator))

    iterator = SkipMissingIterator(InOrderIterator(expr_tree))
    print(" ".join(iterator))
