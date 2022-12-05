class GrandFather:
    pass

class Father(GrandFather):
    pass

class Son(Father):
    pass

print("Son is a subclass of GrandFather\t:", issubclass(Son, GrandFather))

s = Son()
print("s is an instance of Son\t\t\t:", isinstance(s, Son))
print("s is an instance of GrandFather\t\t:", isinstance(s, GrandFather))
