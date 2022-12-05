import os


class PhoneBook:

    def __init__(self, directory=None) -> None:
        self.numbers = {}
        directory = directory or os.path.dirname(os.path.realpath(__file__))
        self.filename = os.path.join(directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
    
    def get_names(self):
        return self.numbers.keys()
    
    def get_numbers(self):
        return self.numbers.values()
    
    def clear(self):
        self.cache.close()
        os.remove(self.filename)