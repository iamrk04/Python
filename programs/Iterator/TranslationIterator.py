from InOrderIterator import InOrderIterator
from SkipMissingIterator import SkipMissingIterator, missing


class TranslationIterator:

    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iter(iterable)
    
    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)

    def __iter__(self):
        return self


#               -
#       *               /
#   p       q       r       +
#                       s       t

if __name__ == "__main__":
    typesetting_table = {
        "-": "\u2212",
        "*": "\u00D7",
        "/": "\u00F7"
    }

    m = missing

    expr_tree = ["-", "*", "/", "p", "q", "r", "+", m, m, m, m, m, m, "s", "t"]
    iterator = TranslationIterator(typesetting_table, SkipMissingIterator(InOrderIterator(expr_tree)))
    print(" ".join(iterator))