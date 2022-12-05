import math
from traceback import print_tb


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope can't be vertical") from e


if __name__ == "__main__":
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)
        print()
        print_tb(e.__traceback__)

        print("-----Finished-----")