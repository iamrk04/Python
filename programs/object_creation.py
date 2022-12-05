class Test:

    def __new__(cls, *args, **kwargs):
        print(f"cls = {cls.__name__}")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")

        obj = object.__new__(cls)

        print(f"id = {id(obj)}")

        return obj

    def __init__(self, arg1, arg2):
        self.x = arg1
        self.y = arg2
        print(f"id = {id(self)}")


if __name__ == "__main__":
    t = Test(1, 2)
