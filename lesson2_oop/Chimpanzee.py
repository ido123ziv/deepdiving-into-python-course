from Monkey import Monkey


class Chimpanzee(Monkey):
    def __init__(self, name, height, color="brown", num_of_legs=2):
        super().__init__(name, color, num_of_legs)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    def print_data(self):
        super().print_data()
        print("""I'm a Chimpanzee and My height is: {}""".format(self.height))

    def eat(self):
        print("""{} the Chimpanzee is eating !""".format(self.name))


