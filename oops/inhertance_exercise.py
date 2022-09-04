class Animal:
    def walk(self):
        print("Animals can walk")


class WildAnimal(Animal):

    def __init__(self):
        self.age = None
        self.name = None
        self.family = None

    def __str__(self):
        # print("Animal {0} of family {1} is of age {2}".format(self.name, self.family, self.age))
        return "Animal {0} of family {1} is of age {2}".format(self.name, self.family, self.age)

    def set_animal(self, family, name, age):
        self.family = family
        self.name = name
        self.age = age

    def print_animal(self):
        print("Animal {0} of family {1} is of age {2}".format(self.name, self.family, self.age))

    @staticmethod
    def temp():
        print("Wild Animal can walk")


if __name__ == '__main__':
    # Add 10 wild animals(name,age) and iterate over it
    wildAnimal1 = WildAnimal()
    wildAnimal1.set_animal("Tiger_1", "Bagheera_1", 15)
    wildAnimal1.print_animal()

    wildAnimal2 = WildAnimal()
    wildAnimal2.set_animal("Tiger_2", "Bagheera_2", 15)
    wildAnimal2.print_animal()

    wildAnimal3 = WildAnimal()
    wildAnimal3.set_animal("Tiger_3", "Bagheera_3", 15)
    wildAnimal3.print_animal()

    wildAnimal4 = WildAnimal()
    wildAnimal4.set_animal("Tiger_4", "Bagheera_4", 15)
    wildAnimal4.print_animal()

    wildAnimal5 = WildAnimal()
    wildAnimal5.set_animal("Tiger_5", "Bagheera_5", 15)
    wildAnimal5.print_animal()

    list_temp = list((wildAnimal1, wildAnimal2, wildAnimal3, wildAnimal4, wildAnimal5))

    print("Looping over the elements")

    for i in list_temp:
        print(i)
