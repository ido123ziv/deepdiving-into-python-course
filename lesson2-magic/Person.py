class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def print_data(self):
        print("My name is {}, I'm {} years old.".format(self.name, self.age))

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age > other.age

    def __add__(self, other):
        return Person(
                self.name + other.name,
                self.age + other.age)

    def __str__(self):
        return "My name is {}, I'm {} years old.".format(self.name, self.age)