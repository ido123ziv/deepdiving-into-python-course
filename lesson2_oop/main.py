from Animal import Animal
from Zebra import Zebra
from Monkey import Monkey
from Chimpanzee import Chimpanzee
from Zoo import Zoo


z1 = Zoo()
z1.add_animal(Zebra("Maya", 34))
z1.add_animal(Monkey("Yoyo", "brown"))
z1.add_animal(Chimpanzee("Chimpanzee", 70, color="purple"))
z1.add_animal(Zebra("Miri", 57))
z1.add_animal(Animal("Yolanda", 3))

print(f"animals count in zoo: {z1.count_animals()}")
print("feeding:")
z1.feed()

print("let's meet the animals")
z1.introduce()
