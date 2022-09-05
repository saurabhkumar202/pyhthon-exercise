class AttrPoc:
    def __init__(self):
        self.red = 200
        self.green = 20
        self.blue = 30

    def __getattr__(self, item):
        if item == "rgbcolor":
            return "Heloo"

    def __setattr__(self, key, value):
        if key == "rgbcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]

        else:
            super().__setattr__(key, value)


def main():
    obj = AttrPoc()
    obj.rgbcolor = (10, 20, 30)
    print(obj.rgbcolor)
    print(obj.red)


if __name__ == "__main__":
    main()
