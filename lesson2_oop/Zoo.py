class Zoo:
    def __init__(self, animals=None):
        if animals is None:
            animals = []
        self._animals = animals

    @property
    def animals(self):
        return self._animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def count_animals(self):
        return len(self.animals)

    def feed(self):
        for animal in self.animals:
            animal.eat()

    def introduce(self):
        for animal in self.animals:
            animal.print_data()
