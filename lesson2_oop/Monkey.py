from Animal import Animal


class Monkey(Animal):
    def __init__(self, name, color="brown", number_of_legs=2):
        super().__init__(name, number_of_legs)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    def print_data(self):
        super().print_data()
        print("""I am a Monkey :)
And I am {}.""".format(self.color))

    def eat(self):
        print("""{} the Monkey is eating !""".format(self.name))

