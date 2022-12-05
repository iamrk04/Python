from dataclasses import dataclass
from position import Position


@dataclass(eq=True)
class Location:
    name: str
    position: Position

if __name__ == "__main__":
    paris = Location(name="Paris", position=Position(48.8, 2.3))
    print(paris)
    paris1 = Location(name="Paris", position=Position(48.8, 2.3))
    print(paris1)
    print(paris == paris1)
    # This will return True because name is ofcourse same and we have taken care of __eq__ in Position class
    # to make sure the Position object os compared correctly