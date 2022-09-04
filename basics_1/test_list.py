class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


def science_student_logic():
    science_student_1 = Student("Saurabh")
    science_student_2 = Student("Ravi")
    science_student_3 = Student("James")

    science_student_list = list((science_student_1, science_student_2, science_student_3))
    for science_student in science_student_list:
        print(f"Way 1 - {science_student}")

    temp = enumerate(science_student_list)
    for index, name in enumerate(science_student_list):
        print(f"Way 2 - {index}, {name}")

    # Get the length and then iterate on it

    science_student_list_length = len(science_student_list)
    print(f"Length is {science_student_list_length}")

    initial_value = 0
    while initial_value < science_student_list_length:
        print(f"Way 3 - Student name is {science_student_list[initial_value]}")
        initial_value += 1

    for item in range(science_student_list_length):
        print(f"Way 4 - Student name is {science_student_list[item]}")


def commerce_student_logic():
    commerce_student_1 = Student("C Jayesh")
    commerce_student_2 = Student("C Ashwini")
    commerce_student_3 = Student("C Tejas")

    commerce_student_list = list((commerce_student_1, commerce_student_2, commerce_student_3))

    # Append items
    commerce_student_4 = Student("C Ajay")
    commerce_student_list.append(commerce_student_4)
    for item in range(len(commerce_student_list)):
        print(f"{commerce_student_list[item]}")

    # Find index of element
    print(commerce_student_list.index(commerce_student_4))

#     Find element by value
    commerce_student_list.pop(0)


if __name__ == '__main__':
    commerce_student_logic()
