import contextlib


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, "exited normally")
    except Exception:
        print(name, "received an exception")
        if propagate:
            raise


if __name__ == "__main__":
    with propagater("outer", True), propagater("inner", False):
        raise TypeError()

    print("--------------------------")
    
    with propagater("outer", False), propagater("inner", True):
        raise TypeError()
