class Vector:
    """
    An n-dimensional vector.
    """

    def __init__(self, **components):
        private_components = {f"_{k}": v for k, v in components.items()}
        self.__dict__.update(private_components)
    
    def __repr__(self):
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                "{k}={v}".format(
                    k=k[1:], v=v) for k, v in self.__dict__.items()
            )
        )

    def __getattr__(self, name):
        private_name = f"_{name}"
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError(f"{self} object has not attribute {name}")

    def __setattr__(self, name, value):
        raise AttributeError(f"Can't set attribute {name}")

    def __delattr__(self, name):
        raise AttributeError(f"Can't delete attribute {name}")


v = Vector(p=2, q=3, r=4)
print(v)
print(dir(v))

print()
print(v.p)
v.p = 18