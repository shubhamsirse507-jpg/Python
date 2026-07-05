from a import a


class c(a):
    def __init__(self, name="C"):
        super().__init__(name)

    def c_method(self):
        return f"{self.name} -> method c"


if __name__ == "__main__":
    obj = c("child_c")
    print(obj.show())
    print(obj.c_method())
    print(obj.common())
