from dataclasses import dataclass, field


def default_mother_func():
    return "pushpaRaj"


@dataclass()
class Student:
    id: str
    name: str
    father_name: str
    mother_name: str = field(default_factory=default_mother_func)

    def __post_init__(self):
        self.UUID = f"{self.id} {self.name}"


student_1 = Student(1, "saurabh", "kamod", "pushplata")
student_2 = Student(2, "aarna", "ritesh")

if __name__ == "__main__":
    print(student_1.name)
    # student_1.name = "rohit"
    # print(student_1.name)
    print(student_1.UUID)
    print(student_2.mother_name)
