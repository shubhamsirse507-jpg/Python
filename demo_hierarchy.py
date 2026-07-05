from a import a
from b import b
from c import c
from d import d


def demo():
    print("-- Base instance --")
    base = a("baseA")
    print(base.show())
    print(base.common())

    print("\n-- Derived instances (hierarchical inheritance) --")
    obj_b = b("B_instance")
    print(obj_b.show())
    print(obj_b.b_method())
    print(obj_b.common())

    obj_c = c("C_instance")
    print(obj_c.show())
    print(obj_c.c_method())
    print(obj_c.common())

    obj_d = d("D_instance")
    print(obj_d.show())
    print(obj_d.d_method())
    print(obj_d.common())


if __name__ == "__main__":
    demo()
