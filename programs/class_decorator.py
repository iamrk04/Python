import inspect

from numpy import typename
from position import *


def auto_repr(cls):
    members = vars(cls)     # gets the members of the class (only native members, not the inherited ones)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    paramter_names = list(sig.parameters)[1:]

    if not all(
        isinstance(members.get(name, None), property)
        for name in paramter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not "
            "all _init__ paramters have matching properties"
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=type(self).__name__,
            args=", ".join(
                "{name}={value}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in paramter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location:
    
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    # def __repr__(self):
    #     return f"{type(self).__name__}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))