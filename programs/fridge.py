"""Demonstrate raiding a refrigerator"""

from contextlib import closing

class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == "deep fried pizza":
            raise RuntimeError("Health Warning!")
        print(f"Taking {food}")
    
    # Function with name 'close' is mandatory for closing to work
    def close(self):
        print("Close fridge door.")

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close()

if __name__ == "__main__":
    raid(input())