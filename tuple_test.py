def test_method_1():
    x = ("saurabh", "saswat", "swati")
    print(x)


def test_tuple_list():
    student = [(1, "Saurabh", "Physics"), (2, "Ravi", "Chemistry")]
    for x, y, z in student:
        print(f"{y} is having roll no {x} studies {z}")


def test_tuple():
    bio_student = (1, "Keshav", "Biology")
    for x in bio_student:
        print(x)


test_tuple()
