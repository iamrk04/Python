from LevelOrderIterator import _is_perfect_length


def _left_child(index):
    return 2 * index + 1

def _right_child(index):
    return 2 * index + 2


class PreOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                "a perfect binary tree with length (2^n) -1 "
            )

        self._sequence = sequence
        self._stack = [0]

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration
        
        index = self._stack.pop()
        result = self._sequence[index]

        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)
        
        left_child_index = _left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result
    
    def __iter__(self):
        return self


#               *
#       +               -
#   a       b       c       d

if __name__ == "__main__":
    expr_tree = ["*", "+", "-", "a", "b", "c", "d"]
    iterator = PreOrderIterator(expr_tree)
    print(next(iterator), end = " ")
    for item in iterator:
        print(item, end = " ")

    print()
    
    iterator = PreOrderIterator(expr_tree)
    print(" ".join(iterator))

    iterator = PreOrderIterator([1, 2,])