from collections import namedtuple

Person = namedtuple('Person', ['fname', 'lname'])
print(Person.__doc__)

p1 = Person("Rahul", "Kumar")
print(p1.fname)
print(p1.lname)