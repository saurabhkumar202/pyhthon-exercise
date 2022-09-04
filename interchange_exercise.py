def swap(y):
    x_length = len(y)
    temp = y[0]
    y[0] = y[x_length - 1]
    y[x_length - 1] = temp


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    swap(x)
    print("Final result is {}".format(x))
