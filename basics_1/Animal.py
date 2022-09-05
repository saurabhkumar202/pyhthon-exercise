class Animal:
    def __init__(self, animal_type, can_walk, can_swim):
        self.type = animal_type
        self.can_walk = can_walk
        self.can_swim = can_swim

    def __str__(self):
        return f"{self.type} can walk- {self.can_walk} and can swim- {self.can_swim}"


a = Animal("Wild", True, False);
print(a)


