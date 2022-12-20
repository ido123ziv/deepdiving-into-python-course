class Animal:
    def __init__(self, name, num=2):
        self.__name = name
        self.__num = num

    @property
    def num(self):
        return self.__num

    @property
    def name(self):
        return self.__name

    def eat(self):
        print(f"{self.__name} is eating !")

    def print_data(self):
        print("""
Hello!
My name is {},
I have {} legs.""".format(self.name, self.num))
