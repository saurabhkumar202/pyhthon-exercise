def test_list():
    x = [[1, 2, 3, 4, 5], ["Saurabh", "Ravi", "Keshav", "Abhinav", "Nishant"]]
    for temp_1, temp_2, temp_3, temp_4, temp_5 in x:
        print(f"{temp_1} {temp_2} {temp_3} {temp_4} {temp_5}")


def test_sorted_list():
    x = [1, 2, 3, 4, 5, 6]
    x.reverse()
    print(x)


def test_sorted_using_sorted_api_list():
    x = [9, 8, 7, 6, 5, 6, 7]
    for temp in sorted(x, key=None, reverse=True):
        print(temp)
    print(x)


# test_list()
# test_sorted_list()
test_sorted_using_sorted_api_list()
