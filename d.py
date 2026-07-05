from a import a


class d(a):
    def __init__(self, name="D"):
        super().__init__(name)

    def d_method(self):
        return f"{self.name} -> method d"


if __name__ == "__main__":
    obj = d()
    print(obj.show())
    print(obj.d_method())
    print(obj.common())
