from abc import ABC, abstractmethod

class A(ABC):

    def xyz(self):
        print("hello xyz")

    @abstractmethod
    def show(self):
        pass

class B(A):

    def show(self):
        print("hi im show from B")

obj = B()

obj.xyz()
obj.show()