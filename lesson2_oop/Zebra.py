from Animal import Animal


class Zebra(Animal):
    def __init__(self, name, strips, number_of_legs=4):
        super().__init__(name, number_of_legs)
        self._strips = strips

    @property
    def strips(self):
        return self._strips

    @strips.setter
    def strips(self, new_strips):
        self._strips = new_strips

    def print_data(self):
        super().print_data()
        print("""I am a Zebra :)
And I have {} strips.
            """.format(self.strips))

    def eat(self):
        print("""{} the Zebra is eating !""".format(self.name))

