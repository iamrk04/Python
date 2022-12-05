class Animal:
    @classmethod
    def description(cls):
        return "An animal"


class Bird(Animal):
    @classmethod
    def description(cls):
        print(super())
        return super().description() + "with wings"


class Flamingo(Bird):
    @classmethod
    def description(cls):
        print(super())
        return super().description() + "and fabulous pink feathers"


Flamingo.description()