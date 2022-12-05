from numpy import iterable
from LevelOrderIterator import _is_perfect_length
from SkipMissingIterator import SkipMissingIterator
from PreOrderIterator import PreOrderIterator


class PerfectBinaryTree:

    def __init__(self, breadth_first_items):
        self._sequence = tuple(breadth_first_items)
        if not _is_perfect_length(self._sequence):
            raise ValueError(
                f"Sequence of length {len(self._sequence)} does not represent "
                "a perfect binary tree with length (2^n) -1 "
            )
    
    def __iter__(self):
        return SkipMissingIterator(PreOrderIterator(self._sequence))


if __name__ == "__main__":
    tree = PerfectBinaryTree("+ * / u v w x".split())
    iterator = iter(tree)
    print(type(iterator))

    for item in iterator:
        print(item, end = " ")
